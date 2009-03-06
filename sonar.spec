# TODO
# - build it from sources
%include	/usr/lib/rpm/macros.java
Summary:	A code quality management platform
Name:		sonar
Version:	1.6
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Java
Source0:	http://dist.sonar.codehaus.org/sonar-1.6.zip
# Source0-md5:	accde4b27b491e63fdba3995759162f5
Source1:	%{name}-web.xml
Source2:	%{name}-context.xml
URL:		http://sonar.codehaus.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-servlet-container
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SONAR is a code quality management platform, dedicated to continuously analyze
and measure technical quality, from the projects portfolio to the class
method.

%prep
%setup -q

%build
cd war
%ant clean war

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_datadir}/%{name},%{_sharedstatedir}/{%{name},tomcat/conf/Catalina/localhost}}
install %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/web.xml
install %SOURCE2 $RPM_BUILD_ROOT%{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
cp -a sonar-web/* $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -sf %{_sysconfdir}/%{name}/web.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/WEB-INF/web.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/web.xml
# do not make this file writeable by tomcat. We do not want to allow user to
# undeploy this app via tomcat manager.
%config(noreplace) %{_sharedstatedir}/tomcat/conf/Catalina/localhost/%{name}.xml
%{_datadir}/%{name}
%attr(755,tomcat,tomcat) %dir %{_sharedstatedir}/%{name}
