%define major 1
%define libname %mklibname wbxml2 %{major}
%define devname %mklibname wbxml2 -d

Name: libwbxml
Version: 0.11.4
Release: 2
Source0: https://github.com/libwbxml/libwbxml/archive/libwbxml-%{version}.tar.gz
Summary: WBXML (Binary XML) library
URL: http://github.com/libwbxml
License: LGPLv2+
Group: System/Libraries
BuildRequires: cmake ninja
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(popt)
BuildRequires: pkgconfig(zlib)

%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications.

%package -n %{libname}
Summary: WBXML (Binary XML) library
Group: System/Libraries

%description -n %{libname}
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -qn %{name}-%{name}-%{version}
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/Modules/*.cmake
%doc %{_docdir}/%{name}
