#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BBmisc
Version  : 1.11
Release  : 6
URL      : https://cran.r-project.org/src/contrib/BBmisc_1.11.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BBmisc_1.11.tar.gz
Summary  : Miscellaneous Helper Functions for B. Bischl
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-BBmisc-lib = %{version}-%{release}
Requires: R-backports
Requires: R-checkmate
BuildRequires : R-backports
BuildRequires : R-checkmate
BuildRequires : buildreq-R

%description
some other guys, mainly for package development.

%package lib
Summary: lib components for the R-BBmisc package.
Group: Libraries

%description lib
lib components for the R-BBmisc package.


%prep
%setup -q -c -n BBmisc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552716965

%install
export SOURCE_DATE_EPOCH=1552716965
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BBmisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BBmisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BBmisc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  BBmisc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BBmisc/DESCRIPTION
/usr/lib64/R/library/BBmisc/INDEX
/usr/lib64/R/library/BBmisc/LICENSE
/usr/lib64/R/library/BBmisc/Meta/Rd.rds
/usr/lib64/R/library/BBmisc/Meta/features.rds
/usr/lib64/R/library/BBmisc/Meta/hsearch.rds
/usr/lib64/R/library/BBmisc/Meta/links.rds
/usr/lib64/R/library/BBmisc/Meta/nsInfo.rds
/usr/lib64/R/library/BBmisc/Meta/package.rds
/usr/lib64/R/library/BBmisc/NAMESPACE
/usr/lib64/R/library/BBmisc/NEWS
/usr/lib64/R/library/BBmisc/R/BBmisc
/usr/lib64/R/library/BBmisc/R/BBmisc.rdb
/usr/lib64/R/library/BBmisc/R/BBmisc.rdx
/usr/lib64/R/library/BBmisc/help/AnIndex
/usr/lib64/R/library/BBmisc/help/BBmisc.rdb
/usr/lib64/R/library/BBmisc/help/BBmisc.rdx
/usr/lib64/R/library/BBmisc/help/aliases.rds
/usr/lib64/R/library/BBmisc/help/paths.rds
/usr/lib64/R/library/BBmisc/html/00Index.html
/usr/lib64/R/library/BBmisc/html/R.css
/usr/lib64/R/library/BBmisc/tests/run-all.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_addClasses.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_asMatrix.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_asQuoted.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_binPack.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_btwn.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_capitalizeStrings.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_checkArg.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_checkListElementClass.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_chunk.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_clipString.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_coalesce.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_collapse.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_collapsef.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_computeMode.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_convertDataFrameCols.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_convertInteger.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_convertListOfRowsToDataFrame.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_convertMatrixType.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_convertRowsToList.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_convertToShortString.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_dapply.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_directory.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_do.call2.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_dropNamed.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_ensureVector.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_explode.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_extractSubList.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_factor.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_filterNull.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getAttributeNames.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getClass1.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getFirstLast.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getMaxColRowIndex.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getMaxIndex.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getOperatingSystem.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getRelativePath.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getUnixTime.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_getUsedFactorLevels.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_hasAttributes.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_insert.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_is.subsetsuperset.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_isFALSE.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_isProperlyNamed.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_isScalarNA.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_isScalarValue.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_isValidNames.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_is_error.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_itostr.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_load2_save2.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_lsort.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_makeDataFrame.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_makeProgressBar.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_makeSimpleFileLogger.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_mapValues.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_namedList.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_nin.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_normalize.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_optimizeSubInts.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_printHead.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_printStrToChar.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_printToChar.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_printf.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_rangeVal.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_requirePackages.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_rowLapply.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_seq.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_setAttribute.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_setClasses.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_setRowColNames.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_setValue.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_sortByCol.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_splitPath.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_splitTime.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_strrepeat.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_suppressAll.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_symdiff.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_system3.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_toRangeStr.R
/usr/lib64/R/library/BBmisc/tests/testthat/test_which.first.last.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/BBmisc/libs/BBmisc.so
