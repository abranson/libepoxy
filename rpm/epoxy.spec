Name:           libepoxy
Version:        1.5.10
Release:        1%{?dist}
Summary:        OpenGL/EGL function pointer management

License:        MIT
URL:            https://github.com/anholt/libepoxy
Source0:        https://download.gnome.org/sources/libepoxy/1.5/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)

%description
libepoxy provides a library for handling OpenGL function pointer management.
This SailfishOS build is EGL/GLES-only.

%package devel
Summary:        Development files for libepoxy
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Headers and development files for libepoxy.

%prep
%autosetup -n libepoxy-%{version}/upstream

%build
%meson \
  --buildtype=release \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  -Degl=yes \
  -Dglx=no \
  -Dx11=false \
  -Ddocs=false \
  -Dtests=false

%meson_build

%install
%meson_install

find %{buildroot}%{_libdir} -name "*.a" -delete || true

%files
%license COPYING*
%doc README*
%{_libdir}/libepoxy.so.*

%files devel
%{_includedir}/epoxy
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc

