#
# todo:
# - fix location of desktop file
#
Summary:	RPM extension for Nautilus
Summary(pl):	Wsparcie Nautilusa dla formatu RPM
Name:		nautilus-rpm
Version:	0.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.1/%{name}-%{version}.tar.bz2
Patch0:		%{name}-sysconfig.patch
URL:		http://www.gnome.org/
BuildRequires:	nautilus-devel
BuildRequires:	rpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RPM extension for Nautilus.

%description -l pl
Wsparcie Nautilusa dla formatu RPM.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/nautilus-rpm*
%{_sysconfdir}/gnome-vfs-2.0/modules/rpmdb.conf
%{_datadir}/applications/*.desktop
%{_libdir}/gnome-vfs-2.0/modules/*
%{_libdir}/bonobo/servers/*
%{_datadir}/mime-info/*
