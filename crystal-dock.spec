%define kf6_version 6.2
%define qt6_version 6.6
%define plasma_version 6.0

Name:		crystal-dock
Version:	2.11
Release:	1
Summary:	Mac-like dock for Wayland
Group:		System/Configuration/Other
License:	GPLv3
URL:		https://github.com/dangvd/crystal-dock
Source0:	https://github.com/dangvd/crystal-dock/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake(ECM) >= %{kf6_version}
BuildRequires:	cmake(Qt6) >= %{qt6_version}
BuildRequires:	cmake(Qt6Core) >= %{qt6_version}
BuildRequires:	cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:	cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:	cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:	cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:	cmake(Qt6Test) >= %{qt6_version}
BuildRequires:	cmake(LayerShellQt) >= %{plasma_version}
BuildRequires:	pkgconfig(wayland-client) >= 1.22
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  stdc++-static-devel
BuildRequires:  qt6-qtbase-theme-gtk3
Requires:       qt6-qttools-dbus
BuildSystem:    cmake
BuildOption:    -S ../src

%description
Crystal Dock is a cool dock (desktop panel) for Linux desktop,
with the focus on attractive user interface, being simple and easy to use,
and cross-desktop support.
Currently supports KDE Plasma 6 and LXQt 2.1 on Wayland.

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
