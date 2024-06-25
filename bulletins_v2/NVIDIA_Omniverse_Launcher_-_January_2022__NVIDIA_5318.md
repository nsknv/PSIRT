

 NVIDIA Omniverse Launcher - January 2022
===========================================================




 Updated 01/31/2022 05:00 PM



NVIDIA has released a software update for NVIDIA Omniverse Launcher to address a security issue that may lead to privilege escalation, impacting confidentiality and integrity.


To protect your system, open the Omniverse Launcher client which will automatically apply the security update. Alternatively, you can download and install this software update from the [Omniverse Downloads](https://www.nvidia.com/en-us/omniverse/) page.


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/v3.1/user-guide) standards.


| CVE ID | Description | Base Score | Vector |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2022‑21817 | NVIDIA Omniverse Launcher contains a Cross-Origin Resource Sharing (CORS) vulnerability which can allow an unprivileged remote attacker, if they can get user to browse malicious site, to acquire access tokens allowing them to access resources in other security domains, which may lead to code execution, escalation of privileges, and impact to confidentiality and integrity. | 9.3 | AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends evaluating the risk to your specific configuration.


### Security Update


The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update.


To protect your system, open the Omniverse Launcher client which will automatically apply the security update. Alternatively, you can download and install this software update from the [Omniverse Downloads](https://www.nvidia.com/en-us/omniverse/) page.


| CVE IDs Addressed | Software Product | Operating System | Affected Versions | Updated Version |
|:--------------------|:--------------------------|:-------------------|:----------------------------|:------------------|
| CVE‑2022‑21817 | NVIDIA Omniverse Launcher | Windows and Linux | All versions prior to 1.5.2 | 1.5.2 |
#### Notes


* Earlier software releases that support this product are also affected. If you are using an earlier release, upgrade to the latest branch release.


### Mitigations


None. See [Security Update](#security-update) for the version to install.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:-----------------|:----------------|
| 1 | January 31, 2022 | Initial release |
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


* [ NVIDIA GeForce Experience - December 2021](/app/answers/detail/a_id/5295/related/1)
* [ NVIDIA SHIELD TV - January 2022](/app/answers/detail/a_id/5259/related/1)
* [Security Notice: NVIDIA Response to Log4j Vulnerabilities - December 2021](/app/answers/detail/a_id/5294/related/1)
* [ NVIDIA Omniverse Nucleus and Omniverse Cache - April 2022](/app/answers/detail/a_id/5342/related/1)
* [ NVIDIA DCGM - August 2021](/app/answers/detail/a_id/5219/related/1)








