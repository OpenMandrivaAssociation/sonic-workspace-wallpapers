%undefine _debugsource_packages

%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define wall_list Altai Autumn BytheWater Canopee Cascade Cluster Coast ColdRipple ColorfulCups DarkestHour Elarun EveningGlow FallenLeaf Flow FlyingKonqui Grey Honeywave IceCold Kay Kite Kokkini MilkyWay Mountain Nexus Nuvole OneStandsOut Opal Orionids PastelHills Patak Path SafeLanding ScarletTree Shell summer_1am Volna

Name: sonic-workspace-wallpapers
Version:	6.7.3
Release:	%{?git:0.%{git}.}1
URL:            https://github.com/Sonic-DE/sonic-workspace-wallpapers
# %if 0%{?git:1}
# Source0:	https://invent.kde.org/plasma/plasma-workspace-wallpapers/-/archive/%{gitbranch}/plasma-workspace-wallpapers-%{gitbranchd}.tar.bz2#/plasma-workspace-wallpapers-%{git}.tar.bz2
# %else
Source0: %url/archive/%version/%name-%version.tar.gz
# %endif
Source1: sonic-workspace-wallpapers-template.in
Summary: Additional wallpapers for SonicDE
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: ninja
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildArch: noarch
%{expand:%(\
        for wallpaper in %wall_list; do\
		echo "Suggests: sonicde-wallpaper-$(echo ${wallpaper}|tr A-Z a-z)"
	done\
)}
Conflicts:   plasma-workspace-wallpapers

BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
%summary

%files
#----------------------------------------------------------------------------

%{expand:%(\
        for wallpaper in %wall_list; do\
                echo "%%{expand:%%(sed -e "s!__LNAME__!${wallpaper,,}!g" -e "s!__NAME__!$wallpaper!g" %{SOURCE1} 2> /dev/null)}";\
        done\
        )
}
