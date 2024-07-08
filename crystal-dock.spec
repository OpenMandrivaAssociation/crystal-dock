Name:		crystal-dock
Version:	2.1
Release:	1
Summary:	Mac-like dock for Wayland
Group:		System/Configuration/Other
License:	GPLv2
URL:		https://github.com/dangvd/crystal-dock
Source0:	https://github.com/dangvd/crystal-dock/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(LayerShellQt) >= 6.1.2
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	stdc++-static-devel

%description
Crystal Dock is a cool dock (desktop panel) for Linux desktop, with the focus on attractive user interface, 
being simple and easy to use and customize, and cross-desktop support.

The current version (version 2) supports KDE Plasma 6 on Wayland. Other desktop environments will be considered when they run on Wayland and provide sufficient APIs. 
The previous version (version 1) supports KDE Plasma 5, GNOME, LXQt, Cinnamon and MATE on X11.


%prep
%autosetup -p1

%build
cd src
%cmake \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DBUILD_STATIC_LIBS:BOOL=ON

%make_build

%install
%make_install -C src/build

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
