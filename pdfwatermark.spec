Name:           pdfwatermark
Version:        1
Release:        1%{?dist}
License:        MIT X11
Summary:        Embed a watermark in PDFs
Group:          Applications/Publishing
Source0:        pdfwatermark.py
Source1:        LICENSE
Source2:        README.md
URL:            https://github.com/intra2net/pdfwatermark
BuildArch:      noarch

%if 0%{?el7}
BuildRequires:  python34-devel
BuildRequires:  python34-PyPDF2
%else
BuildRequires:  python3-devel
BuildRequires:  python3-PyPDF2
%endif

%description
Embed a pdf as background or watermark and place it on each page of another pdf.

%prep
%setup -T -c
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build
%{__python3} -m compileall -b pdfwatermark.py

%install
mkdir -p %{buildroot}%{_bindir}
cp pdfwatermark.pyc %{buildroot}%{_bindir}

# rename pdfwatermark.py to pdfwatermark
cp pdfwatermark.py %{buildroot}%{_bindir}/pdfwatermark

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/pdfwatermark
%{_bindir}/pdfwatermark.pyc
