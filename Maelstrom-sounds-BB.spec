Summary:	Rockin' asteroids game - extra sounds
Summary(pl):	Gra, w której strzelasz do asteroidów - dodatkowe d¼wiêki
Name:		Maelstrom-sounds-BB
Version:	1
Release:	1
License:	unknown
Group:		X11/Applications/Games
Source0:	http://www.devolution.com/~slouken/projects/Maelstrom/add-ons/Beavis_Butthead_Sounds.zip
# Source0-md5:	459890fdb14322cf1b1260e0d232a2e0
URL:		http://www.devolution.com/~slouken/projects/Maelstrom/add-ons.html
Requires:	Maelstrom
Obsoletes:	Maelstrom-sounds
Obsoletes:	Maelstrom-sounds-AoD
Obsoletes:	Maelstrom-sounds-Funky
Obsoletes:	Maelstrom-sounds-Martin
Obsoletes:	Maelstrom-sounds-Simpsons
Obsoletes:	Maelstrom-sounds-Stooges
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom

%description
Extra sounds for Maelstrom: Beavis & Butthead.

%description -l pl
D¼wiêki dla Maelstroma: Beavis & Butthead.

%prep
%setup -q -n Beavis_Butthead_Sounds

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install Maelstrom_Sounds.bin $RPM_BUILD_ROOT%{_gamedir}/"%Maelstrom_Sounds"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{_gamedir}/*
