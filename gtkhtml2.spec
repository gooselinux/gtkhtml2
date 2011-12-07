%define gail_version 1.3
%define gnome_vfs2_version 2.5.0
%define gtk2_version 2.3.0
%define libxml2_version 2.4.20
%define pango_version 1.0.99

### Abstract ###

Name: gtkhtml2
Version: 2.11.1
Release: 7%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
Summary: An HTML widget for GTK+ 2.0
BuildRoot: %{_tmppath}/%{name}-root
Source: http://ftp.gnome.org/pub/GNOME/sources/libgtkhtml/2.11/libgtkhtml-%{version}.tar.bz2

### Dependencies ###

Requires: gail >= %{gail_version}
Requires: gnome-vfs2 >= %{gnome_vfs2_version}
Requires: gtk2 >= %{gtk2_version}
Requires: libxml2 >= %{libxml2_version}

### Build Dependencies ###

BuildRequires: fontconfig
BuildRequires: gail-devel >= %{gail_version}
BuildRequires: gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libtool
BuildRequires: libxml2-devel >= %{libxml2_version}
BuildRequires: pango-devel >= %{pango_version}

%description
GtkHTML2 (sometimes called libgtkhtml) is a widget for
displaying html pages.

%package devel
Group: Development/Libraries
Summary: Libraries, includes, etc to develop Gtkhtml2 applications
Requires: gtkhtml2 = %{version}-%{release}
Requires: gail-devel >= %{gail_version}
Requires: gnome-vfs2-devel >= %{gnome_vfs2_version}
Requires: gtk2-devel >= %{gtk2_version}
Requires: libxml2-devel >= %{libxml2_version}

%description devel
Libraries and include files that can be used to develop Gtkhtml2 applications.

%prep
%setup -q -n libgtkhtml-%{version}

%build
# XXX remove this when bug #83188 is resolved
%ifarch x86_64
%define optflags -g
%endif
%configure
export tagname=CC
make LIBTOOL=/usr/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT
export tagname=CC
%makeinstall LIBTOOL=/usr/bin/libtool

# remove unpackaged files
rm $RPM_BUILD_ROOT%{_libdir}/libgtkhtml-2.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/gtkhtml-2.0
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.11.1-7
- Provide a complete URI for the Source field.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.11.1-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.11.1-4
- Fix license tag

* Sat Feb 09 2008 Matthew Barnes <mbarnes@redhat.com> - 2.11.1-3
- Rebuild with GCC 4.3

* Wed Aug 22 2007 Matthew Barnes <mbarnes@redhat.com> - 2.11.1-2
- Mass rebuild

* Mon Aug 13 2007 Matthew Barnes <mbarnes@redhat.com> - 2.11.1-1
- Update to 2.11.1

* Thu Mar 15 2007 Karsten Hopp <karsten@redhat.com> 2.11.0-4
- rebuild with current gtk2 to add png support (#232013)

* Thu Jul 13 2006 Matthis Clasen <mclasen@redhat.com> - 2.11.0-3
- Rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.11.0-2.1
- rebuild

* Fri Jun 30 2006 Matthew Barnes <mbarnes@redhat.com> - 2.11.0-2
- Fix missing BuildRequires (RH #197146).
- Some cosmetic changes.

* Sat May 20 2006 Matthew Barnes <mbarnes@redhat.com> - 2.11.0-1
- Update to 2.11.0

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.6.3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.6.3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Feb 28 2005 Matthias Clasen <mclasen@redhat.com> - 2.6.3-1
- Update to 2.6.3

* Wed Aug 18 2004 David Malcolm <dmalcolm@redhat.com> - 2.6.2-1
- updated from 2.6.0 to 2.6.2

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr  1 2004 Alex Larsson <alexl@redhat.com> 2.6.0-1
- update to 2.6.0

* Wed Mar 10 2004 Alex Larsson <alexl@redhat.com> 2.5.6-1
- update to 2.5.6

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Alexander Larsson <alexl@redhat.com> 2.5.5-1
- update to 2.5.5

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Jonathan Blandford <jrb@redhat.com> 2.5.2-1
- new version

* Wed Sep  3 2003 Alexander Larsson <alexl@redhat.com> 2.4.0.-1
- Update to 2.4.0

* Tue Aug 19 2003 Alexander Larsson <alexl@redhat.com> 2.3.5-1
- update for gnome 2.3

* Wed Aug  6 2003 Elliot Lee <sopwith@redhat.com>
- Fix libtool

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar 24 2003 Bill Nottingham <notting@redhat.com> 2.2.0-6
- use /usr/bin/libtool

* Wed Feb 19 2003 Alexander Larsson <alexl@redhat.com>
- Add patch that fixes a GtkStyle ref bug. (#82993)

* Fri Feb 14 2003 Jeremy Katz <katzj@redhat.com> 2.2.0-4
- fix build requires

* Thu Jan 30 2003 Matt Wilson <msw@redhat.com> 2.2.0-3
- disable optimizations on x86_64 to work around gcc bug

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Alexander Larsson <alexl@redhat.com> 2.2.0-1
- Update to 2.2.0

* Wed Jan  8 2003 Alexander Larsson <alexl@redhat.com> 2.1.8-3
- Don't ship the static libs

* Tue Jan  7 2003 Alexander Larsson <alexl@redhat.com> 2.1.8-2
- Require gail 1.0

* Tue Jan  7 2003 Alexander Larsson <alexl@redhat.com> 2.1.8-1
- Update to 2.1.8
- Removed patch, as that problem looks solved upstream.

* Wed Oct 23 2002 Alexander Larsson <alexl@redhat.com> 2.0.1-3
- Remove unpackaged files

* Mon Sep  2 2002 Matt Wilson <msw@redhat.com>
- added a patch to avoid crashes during html document destruction

* Thu Aug  8 2002 Alexander Larsson <alexl@redhat.com>
- Update to 2.0.1, fixes #67866

* Sat Jul 27 2002 Havoc Pennington <hp@redhat.com>
- rebuild with new gail

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 1.99.9

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 1.99.7

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.99.6

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- rebuild for new gail, 1.99.5

* Fri Apr  5 2002 Jeremy Katz <katzj@redhat.com>
- update to 1.99.3

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Rebuild for new gnome2 libraries

* Mon Jan 28 2002 Alex Larsson <alexl@redhat.com>
- Initial build.
