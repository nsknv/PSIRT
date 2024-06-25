

 NVIDIA GeForce Experience - May 2019
=======================================================




 Updated 09/29/2021 01:10 PM



NVIDIA has released a software security update for NVIDIA® GeForce Experience™. This update addresses issues that may lead to information disclosure, escalation of privileges, denial of service, or code execution. To protect your system, download and install this software update through the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/product-security/).
--------------------------------------------------------------------------






---




### Details


This section summarizes the potential impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS V3](https://www.first.org/cvss/user-guide) standards.




This section summarizes the potential impact that this security update addresses. Descriptions use CWE™, and base scores and vectors use CVSS V3 standards.
| \*\*CVE\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector\*\* |
| --- | --- | --- | --- |
| CVE‑2019‑5678 | NVIDIA GeForce Experience contains a vulnerability in the Web Helper component, in which an attacker with local system access can craft input that may not be properly validated. Such an attack may lead to code execution, denial of service or information disclosure. | 7.8 | [AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H) |
| CVE‑2019‑5676 | NVIDIA GeForce Experience installer software contains a vulnerability in which it incorrectly loads Windows system DLLs without validating the path or signature (also known as a binary planting or DLL preloading attack), leading to escalation of privileges through code execution. The attacker requires local system access. | 7.2 | [AV:L/AC:H/PR:H/UI:R/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:H/UI:R/S:C/C:H/I:H/A:H) |


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated versions that include this security update.


Download the updates from the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page, or open the client to automatically apply the security update.




The following table lists the NVIDIA software products affected, versions affected, and the updated versions that include this security update. Download the updates from the GeForce Experience Downloads page, or open the client to automatically apply the security update.
| \*\*Software Product\*\* | \*\*Operating System\*\* | \*\*Affected Versions\*\* | \*\*Updated Version\*\* |
| --- | --- | --- | --- |
| GeForce Experience | Windows | All versions prior to 3.19 | 3.19 |


**Notes:**


* Earlier software branch releases that support this product are also affected. If you are using an earlier branch release, upgrade to the latest branch release.
* CVE-2019-5676: If GeForce Experience software is installed on Windows 7, Microsoft KB2533623 must be installed as a prerequisite to address this CVE.


### Mitigations


None. See [Security Updates](#security-updates) for the version to install.


### Acknowledgements


CVE‑2019‑5678: NVIDIA thanks David Yesland of Rhino Security Labs for reporting this issue.


CVE-2019-5676: NVIDIA thanks multiple reporters for reporting this issue: Kushal Arvind Shah of Fortinet's FortiGuard Labs; Łukasz 'zaeek'; Yasin Soliman; Marius Gabriel Mihai; and Stefan Kanthak.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History




Revision History





| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 1.0 | May 30, 2019 | Initial release |


### Support


If you have any questions about this security bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GeForce Experience Software Security Updates for Multiple Vulnerabilities When GameStream is Enabled](/app/answers/detail/a_id/4685/related/1)
* [ NVIDIA SHIELD TV Software Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4682/related/1)
* [ NVIDIA GeForce Experience - September 2018](/app/answers/detail/a_id/4725/related/1)
* [ NVIDIA SHIELD TV – October 2018](/app/answers/detail/a_id/4704/related/1)
* [Security Notice: NVIDIA Response to “Rendered Insecure: GPU Side Channel Attacks are Practical” - November 2018](/app/answers/detail/a_id/4738/related/1)








