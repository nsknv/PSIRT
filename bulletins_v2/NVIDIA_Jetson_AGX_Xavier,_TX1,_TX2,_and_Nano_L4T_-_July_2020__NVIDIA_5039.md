

 NVIDIA Jetson AGX Xavier, TX1, TX2, and Nano L4T - July 2020
===============================================================================




 Updated 10/05/2021 11:16 AM



NVIDIA has released a software security update for Jetson AGX Xavier, TX1, TX2, and Nano in the NVIDIA JetPack™ software development kit (SDK). The update addresses issues that may lead to escalation of privileges. To protect your system, download and install the latest NVIDIA JetPack SDK from [NVIDIA DevZone](https://developer.nvidia.com/embedded/downloads).
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security.](https://www.nvidia.com/product-security/)
--------------------------------------------------------------------------






---




### Details


This section provides a summary of potential vulnerabilities and their impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.0](https://www.first.org/cvss/v3.0/user-guide) standards.


| CVE | Description | Base Score | Vector |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2020‑5974 | NVIDIA JetPack SDK contains a vulnerability in its installation scripts in which permissions are incorrectly set on certain directories, which can lead to escalation of privileges. | 8.8 | AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H |
The NVIDIA risk assessment is based on the maximum risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products and versions affected, and the updated versions that include this security update.


Download and install the latest NVIDIA JetPack software from [NVIDIA DevZone](https://developer.nvidia.com/embedded/downloads).


| CVEs Addressed | Software Product | Operating System | Affected Versions | Updated Versions |
|:-----------------|:----------------------------------------------------|:-------------------|:-------------------------------|:-----------------------|
| CVE‑2020‑5974 | Jetson TX1, TX2 series, AGX Xavier series, and Nano | Linux for Tegra | NVIDIA JetPack SDK 4.2 and 4.3 | NVIDIA JetPack SDK 4.4 |
**Notes:**


* Customers who prefer to continue using NVIDIA JetPack SDK 4.2 or 4.3 can correct the permissions on the affected directories by running the following commands on the L4T host's root file system:


chmod 755 /etc/nvidia-container-runtime/host-files-for-container.d


chmod 644 /etc/nvidia-container-runtime/host-files-for-container.d/\*.csv


### Mitigations


See [Security Updates](#security-updates) for the version to install.


### Acknowledgements


CVE-2020-5974: NVIDIA thanks Michael de Gans for reporting this issue.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History



| Revision | Date | Description |
|-----------:|:-------------|:----------------|
| 1 | July 8, 2020 | Initial release |

### Support


If you have any questions about this Security Bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, "MATERIALS") ARE BEING PROVIDED "AS IS." NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA Jetson TX1 and Jetson Nano L4T - July 2019](/app/answers/detail/a_id/4835/related/1)
* [ NVIDIA GeForce Experience - December 2019](/app/answers/detail/a_id/4954/related/1)
* [ Jetson AGX Xavier, TK1, TX1, TX2, and Nano L4T- December 2019](/app/answers/detail/a_id/4910/related/1)
* [ NVIDIA NVFlash, GPUModeSwitch Tool - November 2019](/app/answers/detail/a_id/4928/related/1)
* [ NVIDIA GeForce Experience – March 2019](/app/answers/detail/a_id/4784/related/1)








