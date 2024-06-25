

 NVIDIA SHIELD TV - August 2019
=================================================




 Updated 09/29/2021 01:10 PM



NVIDIA has released a software security update for NVIDIA SHIELD® TV. This update addresses issues that may lead to information disclosure, code execution, or escalation of privileges. To protect your system, download and install this software update through **Settings**>**About**>**System update**.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/product-security/).
--------------------------------------------------------------------------






---




### Details


This section summarizes the potential impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS V3](https://www.first.org/cvss/user-guide) standards.


SHIELD TV update includes Android™ Security Patch level **2019-07-05**. For more information about what is included in Android security patch levels, refer to the [Android Security Bulletins](https://source.android.com/security/bulletin).


| CVE | Description | Base Score | Vector |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2018‑6241 | NVIDIA Tegra Gralloc module contains a vulnerability in the driver in which missing the input parameter checking of the register buffer API may lead to arbitrary code execution, denial of service or escalation of privileges. | 9.3 | AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H |
| CVE‑2018‑6269 | NVIDIA Tegra kernel driver tegra-se-elp contains a vulnerability in IOCTL handling for user mode requests in which an non-trusted pointer dereference may be made, which may lead to information disclosure, denial of service, escalation of privilege, or code injection errors. | 8.8 | AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H |
| CVE‑2018‑6267 | NVIDIA Tegra library (libnvomx) contains a vulnerability in which a missing check of user metadata may cause user metadata to be invalid, which may lead to a denial of service or possible escalation of privileges. | 8.4 | AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H |
| CVE‑2017‑6275 | NVIDIA Tegra kernel contains a vulnerability in the CORE DVFS Thermal driver where there is the potential to read or write a buffer using an index or pointer that references a memory location after the end of the buffer, which may lead to a denial of service or possible escalation of privileges. | 8.4 | AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H |
| CVE‑2019‑5679 | NVIDIA Tegra bootloader contains a vulnerability in nvtboot where the Trusted OS image is improperly authenticated, which may lead to code execution, denial of service, escalation of privileges, and information disclosure. | 8.2 | AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H |
| CVE‑2018‑6268 | NVIDIA Tegra library contains a vulnerability in libnvmmlite\_video.so, where referencing memory after it has been freed may lead to denial of service or possible escalation of privileges. | 7.8 | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H |
| CVE‑2019‑5680 | NVIDIA Tegra bootloader contains a vulnerability in nvtboot in which the nvtboot-cpu image is loaded without the load address first being validated, which may lead to code execution,denial of service, and escalation of privileges. | 8.2 | AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H |
| CVE‑2019‑5681 | NVIDIA Shield TV contains a vulnerability in the custom NVIDIA API used in the mount system service where user data could be overridden, which may lead to code execution, denial of service, or information disclosure. | 6.5 | AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H |
| CVE‑2019‑5682 | NVIDIA SHIELD contains a vulnerability in the NVIDIA Games App where it improperly exports an Activity but does not properly restrict which applications can launch the Activity, which may lead to code execution or denial of service. | 6.1 | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N |
| CVE‑2018‑6240 | NVIDIA Tegra contains a vulnerability in BootRom in which a user with kernel level privileges can write an arbitrary value to an arbitrary physical address, which may lead to escalation of privileges. | 8.2 | AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H |
SHIELD TV update includes Android™ Security Patch level **2019-07-05**. For more information about what is included in Android security patch levels, refer to the [Android Security Bulletins](https://source.android.com/security/bulletin).


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the software products and versions affected, and the updated versions that include this security update.


Download the updates from **Settings**>**About**>**System update**.


| Software Product | Operating System | Affected Versions | Updated Version |
|:-------------------|:-------------------|:-------------------------------|:------------------------------|
| SHIELD TV | Android O | SHIELD Experience prior to 8.0 | SHIELD Experience Upgrade 8.0 |
**Note:**


* Earlier releases of this product are also affected. If you are using an unsupported release, upgrade to the latest release.


### Mitigations


None. See [Security Updates](#security-updates) for the versions to install.


### Acknowledgements


NVIDIA thanks the following reporters for reporting the issues.


* CVE-2019-5680: Balázs Triszka
* CVE-2019-5681: Yousra Aafer
* CVE-2019-5682: Leron Gray (daddycocoaman)


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:------------------|:---------------------------------------------------------|
| 3 | September 9, 2019 | Added CVE-2018-6240 to the Details section |
| 2 | August 5, 2019 | Updated the CVSS base score and vector for CVE-2019-5680 |
| 1 | August 2, 2019 | Initial release |
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


* [ NVIDIA SHIELD TV – October 2018](/app/answers/detail/a_id/4704/related/1)
* [ NVIDIA GPU Display Driver - February 2019](/app/answers/detail/a_id/4772/related/1)
* [ NVIDIA Jetson TX1 and TX2 L4T - April 2019](/app/answers/detail/a_id/4787/related/1)
* [ NVIDIA SHIELD TV Software Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4682/related/1)
* [ NVIDIA Jetson TX1, Jetson TK1, Jetson TX2, and Tegra K1 L4T Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4635/related/1)








