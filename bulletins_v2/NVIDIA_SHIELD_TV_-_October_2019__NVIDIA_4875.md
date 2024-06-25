

 NVIDIA SHIELD TV - October 2019
==================================================




 Updated 09/29/2021 02:25 PM



NVIDIA has released a software security update for NVIDIA SHIELD® TV. This update addresses issues that may lead to information disclosure, denial of service, code execution, or escalation of privileges. To protect your system, download and install this software update through **Settings**>**About**>**System update**.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/product-security/).
--------------------------------------------------------------------------






---




### Details


This section summarizes the potential impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS V3](https://www.first.org/cvss/user-guide) standards.




This section summarizes the potential impact that this security update addresses. Descriptions use CWE™, and base scores and vectors use CVSS V3 standards.
| \*\*CVE\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector\*\* |
| --- | --- | --- | --- |
| CVE‑2019‑5699 | NVIDIA Tegra bootloader contains a vulnerability where the software performs an incorrect bounds check, which may lead to buffer overflow resulting in escalation of privileges and code execution. | 7.6 | [AV:P/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:P/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) |
| CVE‑2019‑5700 | NVIDIA Tegra software contains a vulnerability in the bootloader, where it does not validate the fields of the boot image, which may lead to code execution, denial of service, escalation of privileges, and information disclosure. | 7.6 | [AV:P/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:P/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) |


SHIELD TV update includes Android™ Security Patch level **2019-07-05**. For more information about what is included in Android security patch levels, refer to the [Android Security Bulletins](https://source.android.com/security/bulletin).


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated versions that include this security update.


Download the updates through **Settings**>**About**>**System update**.




The following table lists the NVIDIA software products affected, versions affected, and the updated versions that include this security update.
| \*\*Software Product\*\* | \*\*Operating System\*\* | \*\*Affected Versions\*\* | \*\*Updated Version\*\* |
| --- | --- | --- | --- |
| SHIELD TV | Android-P | Shield Experience prior to 8.0.1 | Shield Experience Upgrade 8.0.1 |


**Notes:**


* Earlier releases of this product are also affected. If you are using an earlier release, upgrade to the latest release.


### Mitigations


None. See [Security Updates](#security-updates) for the versions to install.


### Acknowledgements


CVE-2019-5700: NVIDIA thanks Ryan Grachek for reporting this issue.


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
| 1.0 | October 7, 2019 | Initial release |


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


* [ NVIDIA GPU Display Driver - February 2019](/app/answers/detail/a_id/4772/related/1)
* [Security Notice: NVIDIA Response to “Rendered Insecure: GPU Side Channel Attacks are Practical” - November 2018](/app/answers/detail/a_id/4738/related/1)
* [ NVIDIA GeForce Experience - November 2018](/app/answers/detail/a_id/4740/related/1)
* [ NVIDIA GeForce Experience – March 2019](/app/answers/detail/a_id/4784/related/1)
* [ NVIDIA Jetson TX1 and TX2 L4T - April 2019](/app/answers/detail/a_id/4787/related/1)








