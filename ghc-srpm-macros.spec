# ghc has been bootstrapped on all Fedora archs except aarch64.
# The ghc interpreter ghci is only supported on a subset of archs.

%global macros_dir %{_rpmconfigdir}/macros.d

Name:           ghc-srpm-macros
Version:        1.3
Release:        1%{?dist}
Summary:        RPM macros for building Haskell source packages

License:        GPLv3+
BuildArch:      noarch

Source0:        macros.ghc-srpm

%description
Macros used when generating Haskell source RPM packages.


%prep
%{nil}


%build
echo no build stage needed


%install
install -p -D -m 0644 %{SOURCE0} %{buildroot}/%{macros_dir}/macros.ghc-srpm


%files
%{macros_dir}/macros.ghc-srpm


%changelog
* Fri May  2 2014 Jens Petersen <petersen@redhat.com> - 1.3-1
- separate from ghc-rpm-macros
