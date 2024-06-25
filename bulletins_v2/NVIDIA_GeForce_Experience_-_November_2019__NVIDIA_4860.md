

 NVIDIA GeForce Experience - November 2019
============================================================




 Updated 09/29/2021 02:17 PM



NVIDIA has released a software security update for NVIDIA® GeForce Experience™. This update addresses issues that may lead to code execution, information disclosure, or denial of service. To protect your system, download and install this software update through the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/product-security/).
--------------------------------------------------------------------------






---




### Details


This section summarizes the potential impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS V3](https://www.first.org/cvss/user-guide) standards.


| CVE | Description | Base Score | Vector |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2019‑5701 | NVIDIA GeForce Experience contains a vulnerability when GameStream is enabled in which an attacker with local system access can load the Intel graphics driver DLLs without validating the path or signature (also known as a binary planting or DLL preloading attack), which may lead to denial of service, information disclosure or escalation of privileges through code execution. | 7.8 | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H |
| CVE‑2019‑5689 | NVIDIA GeForce Experience contains a vulnerability in the Downloader component in which a user with local system access can craft input that may allow malicious files to be downloaded and saved.This behavior may lead to code execution, denial of service, or information disclosure. | 6.7 | AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H |
| CVE‑2019‑5695 | NVIDIA GeForce Experience contains a vulnerability in the local service provider component in which an attacker with local system and privileged access can incorrectly loads Windows system DLLs without validating the path or signature (also known as a binary planting or DLL preloading attack), which may lead to denial of service or information disclosure through code execution. | 6.5 | AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated versions that include this security update.


Download the updates from the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page or open the client to automatically apply the security update.


| Software Product | Operating System | Affected Versions | Updated Version |
|:-------------------|:-------------------|:-----------------------------|:------------------|
| GeForce Experience | Windows | All versions prior to 3.20.1 | 3.20.1 |
**Notes:**


* Earlier software branch releases that support this product are also affected. If you are using an earlier branch release, upgrade to the latest release.


### Mitigations


None. See [Security Updates](#security-updates) for the version to install.


### Acknowledgements


NVIDIA thanks following reporters for reporting the issues.


* CVE-2019-5701: Hashim Jawad of ACTIVELabs
* CVE-2019-5689: Siyuan Yi of Chengdu University of Technology
* CVE-2019-5695: Peleg Hadar of SafeBreach Labs


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:-----------------|:----------------|
| 1 | November 6, 2019 | Initial release |
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


* [ NVIDIA GeForce Experience – March 2019](/app/answers/detail/a_id/4784/related/1)
* [ NVIDIA SHIELD TV – October 2018](/app/answers/detail/a_id/4704/related/1)
* [ NVIDIA GPU Display Driver - August 2019](/app/answers/detail/a_id/4841/related/1)
* [ NVIDIA GeForce Experience - November 2018](/app/answers/detail/a_id/4740/related/1)
* [ NVIDIA SHIELD TV Software Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4682/related/1)








