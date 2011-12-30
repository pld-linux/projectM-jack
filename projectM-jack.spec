Summary:	JACK audio visualization
Summary(pl.UTF-8):	Wizualizacja dźwięku dla JACK-a
Name:		projectM-jack
Version:	2.0.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/projectm/%{name}-%{version}-Source.tar.gz
# Source0-md5:	0cd451d4600be778b191bf5b21e460e0
URL:		http://projectm.sourceforge.net/
BuildRequires:	QtGui-devel >= 4
BuildRequires:	cmake >= 2.4.0
BuildRequires:	libprojectM-devel >= 1:2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	projectM-qt-devel >= 1:2.0.1
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	libprojectM >= 1:2.0.1
Requires:	projectM-qt >= 1:2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Milkdrop based music visualizer using JACK audio with a Qt4 GUI.

%description -l pl.UTF-8
Wizualizacja dźwięku oparta na Milkdrop, wykorzystująca JACK jako
źródło dźwięku, posiadająca graficzny interfejs Qt4.

%prep
%setup -q -n %{name}-%{version}-Source

%build
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/projectM-jack
%{_desktopdir}/projectM-jack.desktop
