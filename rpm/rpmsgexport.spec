Name:          rpmsgexport
Version:       0.1
Release:       1
Summary:       rpmsgexport
URL:           https://github.com/andersson/rpmsgexport
Source0:       %{name}-%{version}.tar.gz
Source1:       udev.rules
License:       BSD-3-Clause

%description
rpmsgexport implements RPMSG_CREATE_EPT_IOCTL for usage in udev rules to
automatically create endpoint devices as remoteproc devices are booted.

%prep
%setup -q -n %{name}-%{version}/rpmsgexport

%build
make %{?_smp_mflags}

%install
make prefix=/usr install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/lib/udev/rules.d/
install -m644 %{SOURCE1} %{buildroot}/lib/udev/rules.d/99-rpmsg.rules

%clean
make clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/rpmsgexport
/lib/udev/rules.d/99-rpmsg.rules
