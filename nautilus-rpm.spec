%define	ver_rpm	4.3-0.20030610.29

Summary:	RPM extension for Nautilus
Summary(pl.UTF-8):   Wsparcie Nautilusa dla formatu RPM
Name:		nautilus-rpm
Version:	0.1
Release:	10
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-rpm/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	a073a09a9ac287ffcfa52c81e72e8028
Source1:	%{name}-rpmdb.desktop
Source2:	%{name}.png
Patch0:		%{name}-update.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.6.0
BuildRequires:	rpm-devel >= %{ver_rpm}
Requires:	rpm >= %{ver_rpm}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RPM extension for Nautilus.

%description -l pl.UTF-8
Wsparcie Nautilusa dla formatu RPM.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f %{_libdir}/gnome-vfs-2.0/modules/*.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/nautilus-rpm*
%{_sysconfdir}/gnome-vfs-2.0/modules/rpmdb.conf
%{_desktopdir}/*.desktop
%{_libdir}/gnome-vfs-2.0/modules/*.so
%{_libdir}/bonobo/servers/*
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
