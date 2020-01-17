Name:    retire-js-repository
Version: 2.0.2
Release: 2
Summary: Repository for scanner detecting the use of JavaScript libraries with known vulnerabilities http://retirejs.github.io/retire.js/
Group:   Development Tools
License: ASL 2.0
Source0: build.sh
Source1: https://raw.githubusercontent.com/RetireJS/retire.js/master/repository/jsrepository.json
Source2: https://raw.githubusercontent.com/RetireJS/retire.js/master/repository/npmrepository.json

%description
Repository for scanner detecting the use of JavaScript libraries with known vulnerabilities http://retirejs.github.io/retire.js/

%install
install -d -m 0775 %{buildroot}/var/www/repos/retire-js-repository
install -p -m 0664 %{SOURCE1} %{buildroot}/var/www/repos/retire-js-repository/jsrepository.json
install -p -m 0664 %{SOURCE2} %{buildroot}/var/www/repos/retire-js-repository/npmrepository.json

%files
/var/www/repos/retire-js-repository/jsrepository.json
/var/www/repos/retire-js-repository/npmrepository.json
