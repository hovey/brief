%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% SNLletter.cls
%% 
%% Written by:
%% Scott A. Roberts, 1513
%% sarober@sandia.gov
%% 2012/02/08
%%
%% Updated 3/16/2022 by David Hart, 8912 (dbhart@sandia.gov)
%% to get formatting to more closely match the Word template
%% including adding the footer on the first page with NNSA/DOE logos.
%% Also added \letterdate and \thedate, and \addressee and \theaddressee
%%
%% Requires packages:
%% * geometry
%% * graphicx
%% * eso-pic
%% * ifthen
%% * color
%% * hancyhdr
%% * afterpage
%%
%% Class options:
%% * CA:                       Use California address rather than NM
%% * OUO:                      Include OUO markings (not including "box")
%%
%% Class commands:
%% * \mailstop{XXXX}:          Provide 4 digit mail stop for address
%% * \phone{XXXX}:             Provide phone number for letterhead
%% * \fax{XXXX}:               Provide fax number for letterhead
%% * \email{XXXX}:             Provide email address for letterhead
%% * \web{XXXX}:               Provide web address for letterhead
%% * \headname{XXXX}:          Provide your name for letterhead
%% * \jobtitle{XXXX}:          Provide your title for letterhead
%% * \department{XXXX}:        Provide your department for letterhead
%% * \addressee{XXXX}:         Provide the adressee's name for the header (p. 2+)
%% * \letterdate{XXXX}:        Provide the date to use in the header (p. 2+)
%% * \signaturegraphic{XXXX}:  File name for digital signature graphic
%% * \OUOHeaderText:           Custom OUO header text
%% * \OUOExemption:            OUO exemption for box
%% * \OUOName:                 OUO approval name and org for box
%% * \OUODate:                 OUO determination date for box
%% * \OUOGuidance:             OUO guidance, if any
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Define setup
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{SNLletter}[2012/02/08 Standard LaTeX class]

%%% Define booleans
\RequirePackage{ifthen}
\newboolean{IncludeMailStop}
\newboolean{IncludeSignature}
\newboolean{IncludePhone}
\newboolean{IncludeFax}
\newboolean{IncludeEMail}
\newboolean{IncludeWeb}
\newboolean{IncludeHeadName}
\newboolean{IncludeJobTitle}
\newboolean{IncludeDepartment}
\newboolean{IncludeCAAddress}
\newboolean{IncludeOUO}
\newboolean{IncludeOUOBox}
\newboolean{IncludeOUOName}
\newboolean{IncludeOUODate}
\newboolean{IncludeOUOGuidance}
\newboolean{IncludeOUOCustom}
\newboolean{IncludeLetterDate}
\newboolean{IncludeAddressee}

%%% Declare class options
\DeclareOption{CA}{
  \setboolean{IncludeCAAddress}{true}
}
\DeclareOption{OUO}{
  \setboolean{IncludeOUO}{true}
}

%%% Inherit letter class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{letter}}
\ProcessOptions\relax
\LoadClass[letterpaper]{letter}

%%% Required packages
% \RequirePackage[letterpaper,left=0.8in,right=0.8in,top=.8in,headheight=-.15in]{geometry}
\RequirePackage[letterpaper,left=1in,right=1in,top=1.25in,headheight=-.15in]{geometry}
\RequirePackage{graphicx}
\RequirePackage{eso-pic}
\RequirePackage{color}
\RequirePackage{afterpage}
\RequirePackage{fancyhdr}


%%% Define custom color
\definecolor{BorderColor}{RGB}{128,0,0}

%%% Add new commands for making letterhead
\newcommand{\theaddressee}{set \textbackslash addressee}
\newcommand{\addressee}[1]{
	\renewcommand{\theaddressee}{#1}
	\setboolean{IncludeAddressee}{true}
}
\newcommand{\thedate}{set \textbackslash letterdate}
\newcommand{\letterdate}[1]{
	\renewcommand{\thedate}{#1}
	\setboolean{IncludeLetterDate}{true}
}
\newcommand{\mailstop}[1]{
  \newcommand{\MailStopVar}{#1}
  \setboolean{IncludeMailStop}{true}
}
\newcommand{\phone}[1]{
  \newcommand{\PhoneVar}{#1}
  \setboolean{IncludePhone}{true}
}
\newcommand{\fax}[1]{
  \newcommand{\FaxVar}{#1}
  \setboolean{IncludeFax}{true}
}
\newcommand{\email}[1]{
  \newcommand{\EMailVar}{#1}
  \setboolean{IncludeEMail}{true}
}
\newcommand{\web}[1]{
  \newcommand{\WebVar}{#1}
  \setboolean{IncludeWeb}{true}
}
\newcommand{\headname}[1]{
  \newcommand{\HeadNameVar}{#1}
  \setboolean{IncludeHeadName}{true}
}
\newcommand{\jobtitle}[1]{
  \newcommand{\JobTitleVar}{#1}
  \setboolean{IncludeJobTitle}{true}
}
\newcommand{\department}[1]{
  \newcommand{\DepartmentVar}{#1}
  \setboolean{IncludeDepartment}{true}
}
\newcommand{\signaturegraphic}[1]{
  \newcommand{\SignatureGraphicVal}{#1}
  \setboolean{IncludeSignature}{true}
}
\newcommand{\OUOExemption}[1]{
  \newcommand{\OUOExemptionVal}{#1}
  \setboolean{IncludeOUO}{true}
  \setboolean{IncludeOUOBox}{true}
}
\newcommand{\OUOName}[1]{
  \newcommand{\OUONameVal}{#1}
  \setboolean{IncludeOUOName}{true}
}
\newcommand{\OUODate}[1]{
  \newcommand{\OUODateVal}{#1}
  \setboolean{IncludeOUODate}{true}
}
\newcommand{\OUOGuidance}[1]{
  \newcommand{\OUOGuidanceVal}{#1}
  \setboolean{IncludeOUOGuidance}{true}
}
\newcommand{\OUOHeaderText}[1]{
  \newcommand{\OUOHeaderTextVal}{#1}
  \setboolean{IncludeOUOCustom}{true}
}

%%% Add space for address block
\address{
  \hspace*{1.0in}
  \vspace{0.8in}
}

% Include graphics at letterhead top
\AddToShipoutPictureBG*{
  \put(\LenToUnit{4.8in},\LenToUnit{10.0in}){
    \includegraphics[width=3.in]{SNL_Horizontal_BlackBlue}
  }
}

\date{}

%%% Commands that require user input modification
\AtBeginDocument{

  %% Include OUO markings at top and bottom
  \ifthenelse{\boolean{IncludeOUO}}{
    \AddToShipoutPictureBG{
      \put(0,\LenToUnit{10.55in}){
        \begin{minipage}{\paperwidth}
          { \fontfamily{phv}\fontsize{12}{1em}\selectfont
            \begin{center}
              \ifthenelse{\boolean{IncludeOUOCustom}}
                {\textbf{\OUOHeaderTextVal}}
                {\textbf{Official Use Only}}
            \end{center}
          }
        \end{minipage}
      }
    }
    \AddToShipoutPictureBG{
      \put(0,\LenToUnit{0.325in}){
        \begin{minipage}{\paperwidth}
          { \fontfamily{phv}\fontsize{12}{1em}\selectfont
            \begin{center}
              \textbf{Official Use Only}
            \end{center}
          }
        \end{minipage}
      }
    }
  }


  %% Include OUO "box"
  \ifthenelse{\boolean{IncludeOUOBox}}{
  	\newgeometry{left=0.8in,right=0.8in,bottom=2.15in,top=.8in,headheight=-.15in}
  	\afterpage{\aftergroup\restoregeometry}
    \AddToShipoutPictureBG*{
      \put(\LenToUnit{4.1in},\LenToUnit{1.5in}){
        \begin{minipage}{3.1in}
          { \fontfamily{phv}\fontsize{6}{0.7em}\selectfont
            \begin{tabular}{|l|}
              \hline \\
              \multicolumn{1}{|c|}{\fontfamily{phv}\fontsize{6}{1em}\selectfont\textbf{OFFICIAL USE ONLY}} \\
              May be exempt from public release under the Freedom of Information Act (5 U.S.C. 522), \\
              exemption number and category: 
              \underline{\OUOExemptionVal} \\[1em]
              \multicolumn{1}{|c|}{Department of Energy review required before public release} \\[0.8em]
              Name/Org: 
              \ifthenelse{\boolean{IncludeOUOName}}{\underline{\OUONameVal}}{\underline{\hspace{1in}}}
              \quad Date: 
              \ifthenelse{\boolean{IncludeOUODate}}{\underline{\OUODateVal}}{\underline{\hspace{1in}}}\\[0.8em]
              \ifthenelse{\boolean{IncludeOUOGuidance}}{Guidance: \underline{\OUOGuidanceVal}}{\underline{\hspace{2in}}}\\[0.8em]
              \hline
            \end{tabular}
          }
        \end{minipage}
      }
    }
}


  %% Add letterhead text
  \AddToShipoutPictureBG*{
    \put(\LenToUnit{.68in},\LenToUnit{9.5in}){
      \begin{minipage}{\linewidth}
        { \fontfamily{phv}\fontsize{7}{0.7em}\selectfont
          \begin{tabular}{lll}
            \hspace{4.5in}
            & \\
            & \\
            & \\
            & \multicolumn{2}{l}{Operated for the United States Department of Energy}\\
            & \multicolumn{2}{l}{by National Technology and Engineering Solutions}\\
            & \multicolumn{2}{l}{of Sandia, LLC.}\\ 
            & \\
            \ifthenelse{\boolean{IncludeCAAddress}}{
              & \multicolumn{2}{l}{P.O.~Box 969\ifthenelse{\boolean{IncludeMailStop}}{, MS-\MailStopVar}{}}\\&\multicolumn{2}{l}{Livermore, CA 94551-0969} \\
            }{
              & \multicolumn{2}{l}{P.O.~Box 5800\ifthenelse{\boolean{IncludeMailStop}}{, MS-\MailStopVar}{}} \\& \multicolumn{2}{l}{Albuquerque, NM 87185\ifthenelse{\boolean{IncludeMailStop}}{-\MailStopVar}{}} \\
            } 
        	\\
            \ifthenelse{\boolean{IncludeHeadName}}{
		      \textbf{\footnotesize\HeadNameVar} 
			}{}
            \ifthenelse{\boolean{IncludePhone}}{
				&  Phone: & \PhoneVar \\
			}{}          
			\ifthenelse{\boolean{IncludeJobTitle}}{
              \JobTitleVar
            }{}
            \ifthenelse{\boolean{IncludeFax}}{
              & Fax:& \FaxVar \\
            }{}
            \ifthenelse{\boolean{IncludeDepartment}}{
				\DepartmentVar 
			}{}
            \ifthenelse{\boolean{IncludeEMail}}{
              &  Email: &\EMailVar \\
            }{}
            \ifthenelse{\boolean{IncludeWeb}}{
              &  Web:& \WebVar \\
            }{}
        \\
          \end{tabular}
        }
    
      \end{minipage}
    }
  }
  
  
    \AddToShipoutPictureBG*{
  	\put(\LenToUnit{.85in},\LenToUnit{0.68in}){
  		\begin{minipage}{7in}
  			{ \fontfamily{phv}\fontsize{9}{1em}\selectfont
  				\begin{tabular}{p{0.2\linewidth}p{0.5\linewidth}p{0.2\linewidth}}
  					\includegraphics[height=0.3in]{NNSA_logo} & \centering\textit{Exceptional Service in the National Interest} & \hfill\includegraphics[height=0.5in]{DOEbwlogo}
  				\end{tabular}
  			}
  		\end{minipage}
  		
  		
  	}
  }
  
  %% Modify the signature to include graphic
  \ifthenelse{\boolean{IncludeSignature}}{
    \renewcommand{\closing}[1]{\par\nobreak\vspace{2\parskip}%
      \stopbreaks
      \noindent
      \parbox{2\indentedwidth}{\raggedright
        \ignorespaces #1\\%
        \includegraphics[height=6\medskipamount]{\SignatureGraphicVal}\\
        \ifx\@empty\fromsig
        \fromname
        \else \fromsig \fi\strut}%
      \par}
  }{
  }

  \fancypagestyle{plain}{\fancyhf{}
	\fancyhead[L]{\ifthenelse{\boolean{IncludeAddressee}}{\theaddressee}{Set \texttt{\textbackslash addressee\{\}}}}
	\fancyhead[C]{-~\thepage~-}
	\fancyhead[R]{\ifthenelse{\boolean{IncludeLetterDate}}{\thedate}{Set \texttt{\textbackslash letterdate\{\}}}}
	\renewcommand{\headrulewidth}{0pt}
	}
  \pagestyle{plain}

  %% Select default font
  %\fontfamily{qpl}\selectfont % Palatino font, more compact than the default Computer Modern, and looks more like the Word template font (Times New Roman)
  % \fontfamily{ptm}\selectfont % Times New Roman font, more like the Word template font, but less compact than Palatino
  %\fontfamily{pbk}\selectfont % Bookman
  \fontfamily{cmr}\selectfont % Computer Modern Roman, the default LaTeX font, which is more compact than Times New Roman and looks pretty good on letterhead

} % End AtBeginDocument
