

 NVIDIA GeForce Experience - April 2021
=========================================================




 Updated 10/05/2021 01:58 PM



NVIDIA has released a software security update for NVIDIA® GeForce Experience™ software. This update addresses an issue that may lead to code execution, denial of service, or local privilege escalation.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


To protect your system, download and install this software update through the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page, or open the client to automatically apply the security update.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).
------------------------------------------------------------------

 



---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/specification-document) standards.


| CVE IDs | Description | Base Score | Vector |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2021‑1079 | NVIDIA GeForce Experience contains a vulnerability in GameStream plugins where log files are created using NT/System level permissions, which may lead to code execution, denial of service, or local privilege escalation. The attacker does not have control over the consequence of a modification nor would they be able to leak information as a direct result of the overwrite. | 6.1 | AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the affected NVIDIA software products and versions, and the updated version that includes this security update.


Download the updates through the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page, or open the client to automatically apply the security update.


| CVE IDs Addressed | Software Product | Operating System | Affected Versions | Updated Driver Version |
|:--------------------|:-------------------|:-------------------|:---------------------------|-------------------------:|
| CVE‑2021‑1079 | GeForce Experience | Windows | All versions prior to 3.22 | 3.22 |
**Notes:**


* Earlier software releases that support this product are also affected. If you are using an earlier release, upgrade to the latest release version.


### Mitigations


See [Security Updates](#security-updates) for the version to install.


### Acknowledgements


CVE-2021-1079: NVIDIA thanks Matt Batten and Paolo Stagno for reporting this issue.


### Get the Most Up to Date Product Security Information


Visit the  [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:---------------|:--------------------------------------------------------------------|
| 3 | May 14, 2021 | Clarified the CVE description and updated the CVSS score and vector |
| 2 | April 19, 2021 | Updated the Acknowledgements section |
| 1 | April 16, 2021 | Initial release |
### Support


If you have any questions about this security bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, "MATERIALS") ARE BEING PROVIDED "AS IS." NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GeForce Experience - October 2020](/app/answers/detail/a_id/5076/related/1)
* [ NVIDIA GeForce NOW - November 2020](/app/answers/detail/a_id/5096/related/1)
* [ NVIDIA GeForce NOW - September 2020](/app/answers/detail/a_id/5052/related/1)
* [ NVIDIA GeForce Experience - July 2020](/app/answers/detail/a_id/5038/related/1)
* [ NVIDIA GeForce Experience - December 2019](/app/answers/detail/a_id/4954/related/1)








