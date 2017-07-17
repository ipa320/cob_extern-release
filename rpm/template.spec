Name:           ros-kinetic-cob-extern
Version:        0.6.11
Release:        0%{?dist}
Summary:        ROS cob_extern package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_extern
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-libconcorde-tsp-solver
Requires:       ros-kinetic-libdlib
Requires:       ros-kinetic-libntcan
Requires:       ros-kinetic-libpcan
Requires:       ros-kinetic-libphidgets
Requires:       ros-kinetic-libqsopt
Requires:       ros-kinetic-opengm
BuildRequires:  ros-kinetic-catkin

%description
The cob_extern stack contains third party libraries needed for operating
Care-O-bot. The packages are downloaded from the manufactorers website and not
changed in any way.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jul 17 2017 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.11-0
- Autogenerated by Bloom

