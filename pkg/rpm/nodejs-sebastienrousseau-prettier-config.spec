%global npm_scope     @sebastienrousseau
%global npm_bare      prettier-config
%global sitelib       %{_prefix}/lib/node_modules

Name:           nodejs-sebastienrousseau-prettier-config
Version:        0.0.7
Release:        1%{?dist}
Summary:        Shareable Prettier configuration rules adhering to modern formatting standards

License:        Apache-2.0 OR MIT
URL:            https://github.com/sebastienrousseau/prettier-config
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       nodejs >= 20

%description
@sebastienrousseau/prettier-config is a shareable configuration preset with no runtime
dependencies: inert data plus a loader. Installed under
%{sitelib} so that require() resolves it without further configuration.

%prep
%autosetup -n %{name}-%{version}

%build
# Architecture-independent data; nothing to compile.

%install
install -d %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}
install -pm 0644 index.js %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}/
install -pm 0644 index.mjs %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}/
install -pm 0644 index.cjs %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}/
install -pm 0644 index.d.ts %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}/
install -pm 0644 LICENSE %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}/
install -pm 0644 .editorconfig %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}/
install -pm 0644 package.json %{buildroot}%{sitelib}/%{npm_scope}/%{npm_bare}/

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{sitelib}/%{npm_scope}/%{npm_bare}/

%changelog
* Fri Sep 11 2026 Sebastien Rousseau <sebastian.rousseau@gmail.com> - 0.0.7-1
- Initial packaging.
