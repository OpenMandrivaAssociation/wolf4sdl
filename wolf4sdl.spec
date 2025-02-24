Name:           wolf4sdl
Version:        1.7
Release:        3
Summary:        SDL port of id Software Wolfenstein 3D
Group:          Games/Arcade
License:        Distributable
URL:            https://www.alice-dsl.net/mkroll/
Source0:        http://www.alice-dsl.net/mkroll/bins/Wolf4SDL-1.7-src.zip
Source1:        %{name}.desktop
Patch2:         Wolf4SDL-1.6-registered-apogee.patch
Patch3:         Wolf4SDL-1.6-shareware.patch
Patch4:         Wolf4SDL-1.6-spear.patch
Patch5:         Wolf4SDL-1.6-speardemo.patch
BuildRequires:  SDL-devel SDL_mixer-devel desktop-file-utils

%description
Maybe it was the fact that people got to blow away Nazis. Maybe it was the \
sheer challenge of it all. For whatever reason, Wolfenstein 3D and Spear of \
Destiny, pioneered the first-person shooter genre and brought its legendary \
creators, id Software, worldwide notoriety and numerous awards. In fact, The \
Computer Gaming World Hall of Fame recognized Wolfenstein 3D as helping to \
shape the overall direction of the computer gaming industry. \
\
Wolf4SDL is an open-source port of id Software's classic first-person shooter \
Wolfenstein 3D to the cross-platform multimedia library "Simple DirectMedia \
Layer (SDL)" (http://www.libsdl.org). It is meant to keep the original feel \
while taking advantage of some improvements.

%package        registered-id
Summary:        SDL port of Wolfenstein 3D - id Software registered version
URL:            https://www.idsoftware.com/games/wolfenstein/wolf3d/

%description registered-id
This package contains %{name} compiled for playing the registered version of
Wolfenstein 3D as sold by id Software:
http://www.idsoftware.com/games/wolfenstein/wolf3d/

You will need the original registered version's data files to play the
registered version. Place the data files under /usr/share/wolf3d/registered-id
before starting %{name}-registered-id. Note all file-names must be lowercase!



%package        registered-apogee
Summary:        SDL port of Wolfenstein 3D - Apogee registered version
URL:            https://www.3drealms.com/wolf3d/index.html

%description registered-apogee
This package contains %{name} compiled for playing the registered version of
Wolfenstein 3D as sold by Apogee / 3Drealms here:
http://www.3drealms.com/wolf3d/index.html

You will need the original registered version's data files to play the
registered version. Place the data files under
/usr/share/wolf3d/registered-apogee before starting
%{name}-registered-apogee. Note all file-names must be lowercase!



%package        shareware
Summary:        SDL port of id Software's Wolfenstein 3D - shareware version
URL:            https://www.3drealms.com/wolf3d/index.html
Requires:       wolf3d-shareware

%description shareware
This package contains %{name} compiled for playing the shareware version of
Wolfenstein 3D.



%package        spear
Summary:        SDL port of Wolfenstein 3D - Spear of Destiny version
URL:            https://www.idsoftware.com/games/wolfenstein/spear/

%description spear
This package contains %{name} compiled for playing the Spear of Destiny
prequel to Wolfenstein 3D, sold by id Software:
http://www.idsoftware.com/games/wolfenstein/spear/

You will need the original Spear of Destiny data files to play.
Place the data files under /usr/share/spear/full before starting
%{name}-spear. Note all file-names must be lowercase!



%package        spear-demo
Summary:        SDL port of Wolfenstein 3D - Spear of Destiny demo version
URL:            https://www.idsoftware.com/games/wolfenstein/spear/
Requires:       spear-demo

%description spear-demo
This package contains %{name} compiled for playing the demo of the Spear of
Destiny prequel to Wolfenstein 3D.



%prep
%setup -c -T -n Wolf4SDL-%{version}-src
# Must unpack ourselves to make zip do dos2unix conversion
pushd .. && unzip -a -q %{SOURCE0} && popd
# %patch0 -p1
# %patch1 -p1
# for i in debian/patches/*.patch; do
#     patch -p1 < $i
# done


%build
CFLAGS="$RPM_OPT_FLAGS -Wno-sign-compare -Wno-switch -Wno-unused-result"
CFLAGS="$CFLAGS -fno-toplevel-reorder $(sdl-config --cflags)"

make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-id/\\\""
mv wolf3d %{name}-registered-id
cp %{SOURCE1} %{name}-registered-id.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (id)|g' \
    %{name}-registered-id.desktop
sed -i 's|@VARIANT@|registered-id|g' %{name}-registered-id.desktop
make clean

patch -p1 < %{PATCH2}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/registered-apogee/\\\""
mv wolf3d %{name}-registered-apogee
cp %{SOURCE1} %{name}-registered-apogee.desktop
sed -i 's|@NAME@|Wolfenstein 3D Registered (Apogee)|g' \
    %{name}-registered-apogee.desktop
sed -i 's|@VARIANT@|registered-apogee|g' %{name}-registered-apogee.desktop
make clean

patch -p1 < %{PATCH3}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/wolf3d/shareware/\\\""
mv wolf3d %{name}-shareware
cp %{SOURCE1} %{name}-shareware.desktop
sed -i 's|@NAME@|Wolfenstein 3D Shareware (Apogee)|g' %{name}-shareware.desktop
sed -i 's|@VARIANT@|shareware|g' %{name}-shareware.desktop
make clean

patch -p1 < %{PATCH4}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/full/\\\""
mv wolf3d %{name}-spear
cp %{SOURCE1} %{name}-spear.desktop
sed -i 's|@NAME@|Spear of Destiny|g' %{name}-spear.desktop
sed -i 's|@VARIANT@|spear|g' %{name}-spear.desktop
make clean

patch -p1 < %{PATCH5}
make %{?_smp_mflags} \
    CFLAGS="$CFLAGS -DDATADIR=\\\"/usr/share/spear/demo/\\\""
mv wolf3d %{name}-spear-demo
cp %{SOURCE1} %{name}-spear-demo.desktop
sed -i 's|@NAME@|Spear of Destiny Demo|g' %{name}-spear-demo.desktop
sed -i 's|@VARIANT@|spear-demo|g' %{name}-spear-demo.desktop


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

# Help launchers for shareware and spear-demo

cat > %{buildroot}%{_bindir}/%{name}-shareware <<EOF
#!/bin/bash

cd /usr/share/wolf3d/shareware/ && %{name}-shareware.real

EOF

cat > %{buildroot}%{_bindir}/%{name}-spear-demo <<EOF
#!/bin/bash

cd /usr/share/spear/demo/ && %{name}-spear-demo.real

EOF

chmod a+x %{buildroot}%{_bindir}/%{name}-spear-demo


install -m 755 %{name}-registered-id %{buildroot}%{_bindir}/%{name}-registered-id
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{name}-registered-id.desktop
mkdir -p %{buildroot}%{_datadir}/wolf3d/registered-id

install -m 755 %{name}-registered-apogee %{buildroot}%{_bindir}/%{name}-registered-apogee
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{name}-registered-apogee.desktop
mkdir -p %{buildroot}%{_datadir}/wolf3d/registered-apogee

install -m 755 %{name}-shareware %{buildroot}%{_bindir}/%{name}-shareware.real
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{name}-shareware.desktop

install -m 755 %{name}-spear %{buildroot}%{_bindir}/%{name}-spear
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{name}-spear.desktop
mkdir -p %{buildroot}%{_datadir}/spear/full

install -m 755 %{name}-spear-demo %{buildroot}%{_bindir}/%{name}-spear-demo.real
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{name}-spear-demo.desktop


%clean


%files registered-id
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-registered-id
%{_datadir}/applications/%{name}-registered-id.desktop
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-id

%files registered-apogee
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-registered-apogee
%{_datadir}/applications/%{name}-registered-apogee.desktop
%dir %{_datadir}/wolf3d
%dir %{_datadir}/wolf3d/registered-apogee

%files shareware
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-shareware
%{_bindir}/%{name}-shareware.real
%{_datadir}/applications/%{name}-shareware.desktop

%files spear
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-spear
%{_datadir}/applications/%{name}-spear.desktop
%dir %{_datadir}/spear
%dir %{_datadir}/spear/full

%files spear-demo
%defattr(-,root,root,-)
%doc Changes.txt README.txt license-*.txt
%{_bindir}/%{name}-spear-demo
%{_bindir}/%{name}-spear-demo.real
%{_datadir}/applications/%{name}-spear-demo.desktop




