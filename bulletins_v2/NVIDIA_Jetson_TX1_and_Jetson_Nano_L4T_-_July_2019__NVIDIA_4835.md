

 NVIDIA Jetson TX1 and Jetson Nano L4T - July 2019
====================================================================




 Updated 09/29/2021 02:08 PM



NVIDIA has released software security updates for NVIDIA® Jetson™ TX1 and Jetson™ Nano in the NVIDIA® Tegra® Linux Driver Package (L4T).
----------------------------------------------------------------------------------------------------------------------------------------


The update addresses issues that may lead to code execution, denial of service, or escalation of privileges. To protect your system, download available updates from NVIDIA DevZone.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/product-security/).
--------------------------------------------------------------------------






---




### Details


This section summarizes the potential impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS V3](https://www.first.org/cvss/user-guide) standards.


| CVE | Description | Base Score | Vector |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2019‑5680 | NVIDIA Tegra bootloader contains a vulnerability in nvtboot in which the nvtboot-cpu image is loaded without the load address first being validated, which may lead to code execution,denial of service, or escalation of privileges. | 8.2 | AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated versions that include this security update.


| CVE | Software Product | Operating System | Affected Versions | Updated Version |
|:--------------|:-------------------|:-------------------|:-----------------------------------|:------------------|
| CVE‑2019‑5680 | Jetson TX1 | Linux for Tegra | N/A\* | R32.2 |
| CVE‑2019‑5680 | Jetson TX1 | Linux for Tegra | R28.3 and earlier release versions | R28.3.1 |
| CVE‑2019‑5680 | Jetson Nano | Linux for Tegra | R32.1 | R32.2 |
Download the updates from [NVIDIA DevZone](https://developer.nvidia.com/embedded/downloads).


**Notes:**


* \*R32.2 is the first release version supporting Jetson TX1 in the R32 branch.
* The table above may not be a comprehensive list of all affected supported versions or branch releases and may be updated as more information becomes available.


### Mitigations


None. See [Security Updates](#security-updates) for the versions to install.


### Acknowledgements


CVE-2019-5680: NVIDIA thanks Balázs Triszka for reporting this issue.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:--------------|:-----------------------------------------------------------------------------------------------|
| 4 | July 29, 2019 | Added the security update R28.3.1 for Jetson TX1 and the security update R32.2 for Jetson Nano |
| 3 | July 22, 2019 | Corrected the CVSS vector and base score |
| 2 | July 19, 2019 | Corrected the summary to describe potential impacts more accurately |
| 1 | July 18, 2019 | Initial release |
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


* [ NVIDIA GeForce Experience – March 2019](/app/answers/detail/a_id/4784/related/1)
* [ NVIDIA SHIELD TV – October 2018](/app/answers/detail/a_id/4704/related/1)
* [ NVIDIA GeForce Experience - September 2018](/app/answers/detail/a_id/4725/related/1)
* [ NVIDIA GeForce Experience Software Security Updates for Multiple Vulnerabilities When GameStream is Enabled](/app/answers/detail/a_id/4685/related/1)
* [Security Notice: NVIDIA Response to “Rendered Insecure: GPU Side Channel Attacks are Practical” - November 2018](/app/answers/detail/a_id/4738/related/1)








