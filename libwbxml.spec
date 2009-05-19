%define major 0
%define libname %mklibname wbxml %{major}
%define develname %mklibname wbxml -d

Summary:	WBXML parser and compiler library
Name:		libwbxml
Version:	0.10.7
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libwbxml.opensync.org
Source:		http://prdownloads.sourceforge.net/wbxmllib/%{name}-%{version}.tar.gz
Requires:	expat >= 2.0.1
BuildRequires:	cmake
BuildRequires:	expat-devel >= 2.0.1
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications. 

%package -n %{libname}
Group:		System/Libraries
License:	LGPLv2+
Summary:	Library for parsing WAP Binary XML
Obsoletes:  %mklibname wbxml2_ 0

%description -n %libname
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications. 

This package contains just the library for use by other applications.

%package -n %{develname}
Group:		Development/C
License:	LGPLv2+
Summary:	Library for developing applications that parse WAP Binary XML
Requires:	%{libname} = %{version}-%{release}
Provides:   wbxml-devel = %{version}-%{release}
Obsoletes:  %mklibname wbxml2_ -d 0

%description -n %{develname}
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce bandwidth
in mobile communications. 

This package contains the headers and other development files required to
compile applications that need to parse WBXML.

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%{_bindir}/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README References TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwbxml2.pc
