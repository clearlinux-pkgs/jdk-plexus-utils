#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-plexus-utils
Version  : 3.0.24
Release  : 6
URL      : https://github.com/codehaus-plexus/plexus-utils/archive/plexus-utils-3.0.24.tar.gz
Source0  : https://github.com/codehaus-plexus/plexus-utils/archive/plexus-utils-3.0.24.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-plexus-utils-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-bsh
BuildRequires : jdk-cdi-api
BuildRequires : jdk-cglib
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-parent
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-easymock3
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-enforcer
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-forge-parent
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-objenesis
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-plexus
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
Plexus-Utils
============
[![Build Status](https://travis-ci.org/codehaus-plexus/plexus-utils.svg?branch=master)](https://travis-ci.org/codehaus-plexus/plexus-utils)

%package data
Summary: data components for the jdk-plexus-utils package.
Group: Data

%description data
data components for the jdk-plexus-utils package.


%prep
%setup -q -n plexus-utils-plexus-utils-3.0.24

python3 /usr/share/java-utils/mvn_file.py : plexus/utils
python3 /usr/share/java-utils/mvn_alias.py : plexus:plexus-utils
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:project" "<packaging>bundle</packaging>"
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   "pom:build/pom:plugins" "
<plugin>
<groupId>org.apache.felix</groupId>
<artifactId>maven-bundle-plugin</artifactId>
<extensions>true</extensions>
<configuration>
<instructions>
<_nouses>true</_nouses>
<Export-Package>org.codehaus.plexus.util.*;org.codehaus.plexus.util.cli.*;org.codehaus.plexus.util.cli.shell.*;org.codehaus.plexus.util.dag.*;org.codehaus.plexus.util.introspection.*;org.codehaus.plexus.util.io.*;org.codehaus.plexus.util.reflection.*;org.codehaus.plexus.util.xml.*;org.codehaus.plexus.util.xml.pull.*</Export-Package>
</instructions>
</configuration>
</plugin>"

%build
python3 /usr/share/java-utils/mvn_build.py -f

%install
xmvn-install  -R .xmvn-reactor -n plexus-utils -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/plexus/utils.jar
/usr/share/maven-metadata/plexus-utils.xml
/usr/share/maven-poms/plexus/utils.pom
