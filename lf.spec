%define debug_package %{nil}

Name:		lf
Version:	41
Release:	3
Source0:	https://github.com/gokcehan/lf/archive/r%{version}/%{name}-r%{version}.tar.gz
Source1:	vendor.tar.gz
Summary:	A terminal file manager written in Go inspired by ranger
URL:		https://github.com/gokcehan/lf
License:	MIT
Group:		File tools
BuildRequires:	golang >= 1.24.0

%description
lf (as in "list files") is a terminal file manager written in Go with a heavy
inspiration from ranger file manager. See faq for more information and
tutorial for a gentle introduction with screencasts.

%prep
%autosetup -n %{name}-r%{version} -a1

%build
go build -v -x -trimpath -ldflags="-s -w -X main.gVersion=r%{version}" -o %{name}

%install
install -Dm0755 %{name}      %{buildroot}%{_bindir}/lf
install -Dm0644 lf.1         %{buildroot}%{_mandir}/man1/lf.1
install -Dm0644 lf.desktop   %{buildroot}%{_datadir}/applications/lf.desktop
install -Dm0644 etc/lf.bash  %{buildroot}%{_datadir}/bash-completion/completions/lf
install -Dm0644 etc/lf.zsh   %{buildroot}%{_datadir}/zsh/site-functions/_lf
install -Dm0644 etc/lf.fish  %{buildroot}%{_datadir}/fish/vendor_completions.d/lf.fish
install -Dm0644 etc/lf.csh   %{buildroot}%{_sysconfdir}/profile.d/90lf.csh

install -Dm0644 etc/lfcd.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/lfcd.fish
install -Dm0644 etc/lfcd.csh  %{buildroot}%{_sysconfdir}/profile.d/90lfcd.csh
install -Dm0644 etc/lfcd.sh   %{buildroot}%{_sysconfdir}/profile.d/90lfcd.sh

%files
%license LICENSE
%doc README.md CHANGELOG.md
%doc etc/lfrc.example etc/colors.example etc/icons.example etc/icons_colored.example
%{_bindir}/lf
%{_mandir}/man1/lf.1*
%{_datadir}/applications/lf.desktop
%{_datadir}/bash-completion/completions/lf
%{_datadir}/zsh/site-functions/_lf
%{_datadir}/fish/vendor_completions.d/lf.fish
%{_datadir}/fish/vendor_completions.d/lfcd.fish
%{_sysconfdir}/profile.d/90lf.csh
%{_sysconfdir}/profile.d/90lfcd.csh
%{_sysconfdir}/profile.d/90lfcd.sh
