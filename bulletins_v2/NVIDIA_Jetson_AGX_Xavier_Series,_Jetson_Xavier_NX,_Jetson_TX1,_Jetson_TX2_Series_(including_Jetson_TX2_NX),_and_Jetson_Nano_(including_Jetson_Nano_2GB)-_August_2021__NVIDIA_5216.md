

 NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB)- August 2021
=======================================================================================================================================================================================




 Updated 01/24/2022 03:28 PM



NVIDIA has released a software update for NVIDIA® Jetson AGX Xavier™ series, Jetson Xavier™ NX, Jetson TX1, Jetson TX2 series (including Jetson TX2 NX), and Jetson Nano™ devices (including Jetson Nano 2GB) in the NVIDIA JetPack™ software development kit (SDK). The update addresses security issues that may lead to escalation of privileges, denial of service, and information disclosure. To protect your system, download and install the latest NVIDIA JetPack 4.6 SDK from [Jetson Download Center](https://developer.nvidia.com/embedded/downloads).


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/v3.1/user-guide) standards.


| CVE ID | Description | Base Score | Vector |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2021‑1106 | NVIDIA Linux kernel distributions contain a vulnerability in nvmap, where writes may be allowed to read-only buffers, which may result in escalation of privileges, complete denial of service, unconstrained information disclosure, and serious data tampering of all processes on the system. | 7.8 | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H |
| CVE‑2021‑1107 | NVIDIA Linux kernel distributions contain a vulnerability in nvmap NVMAP\_IOC\_WRITE\* paths, where improper access controls may lead to code execution, complete denial of service, and seriously compromised integrity of all system components. | 7.8 | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H |
| CVE‑2021‑1108 | NVIDIA Linux kernel distributions contain a vulnerability in FuSa Capture (VI/ISP), where integer underflow due to lack of input validation may lead to complete denial of service, partial integrity, and serious confidentiality loss for all processes in the system. | 7.3 | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:H |
| CVE‑2021‑1109 | NVIDIA camera firmware contains a multistep, timing-related vulnerability where an unauthorized modification by camera resources may result in loss of data integrity or denial of service across several streams. | 7.2 | AV:L/AC:H/PR:H/UI:N/S:C/C:N/I:H/A:H |
| CVE‑2021‑1110 | NVIDIA Linux kernel distributions on Jetson Xavier contain a vulnerability in camera firmware where a user can change input data after validation, which may lead to complete denial of service and serious data corruption of all kernel components. | 7.1 | AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H |
| CVE‑2021‑1111 | Bootloader contains a vulnerability in the NV3P server where any user with physical access through USB can trigger an incorrect bounds check, which may lead to buffer overflow, resulting in limited information disclosure, limited data integrity, and denial of service across all components. | 6.7 | AV:P/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:H |
| CVE‑2021‑1112 | NVIDIA Linux kernel distributions contain a vulnerability in nvmap, where a null pointer dereference may lead to complete denial of service. | 5.5 | AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H |
| CVE‑2021‑1113 | NVIDIA camera firmware contains a difficult-to-exploit vulnerability, where a highly privileged attacker can cause unauthorized modification to camera resources, which may result in complete denial of service and partial loss of data integrity for all clients. | 4.7 | AV:L/AC:H/PR:H/UI:N/S:U/C:N/I:L/A:H |
| CVE‑2021‑1114 | NVIDIA Linux kernel distributions contain a vulnerability in the kernel crypto node, where use after free may lead to complete denial of service. | 4.4 | AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update.


| CVE IDs Addressed | Software Product | Operating System | Affected Versions | Updated Version |
|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|:-------------------|:----------------------------------|:------------------|
| CVE‑2021‑1110 | Jetson AGX Xavier series, Jetson Xavier NX | Jetson Linux | All 32.x versions prior to 32.6.1 | 32.6.1 |
| CVE‑2021‑1106 CVE‑2021‑1107 CVE‑2021‑1108 CVE‑2021‑1109 CVE‑2021‑1112 CVE‑2021‑1113 | Jetson AGX Xavier series, Jetson Xavier NX, Jetson TX2 series, Jetson TX2 NX, Jetson Nano, Jetson Nano 2GB, Jetson TX1 | Jetson Linux | All 32.x versions prior to 32.6.1 | 32.6.1 |
| CVE‑2021‑1111 CVE‑2021‑1114 | Jetson AGX Xavier series, Jetson Xavier NX, Jetson TX2 series, Jetson TX2 NX | Jetson Linux | All 32.x versions prior to 32.6.1 | 32.6.1 |
#### Notes


* Earlier software branch releases that support this product are also affected. If you are using an earlier branch release, upgrade to the latest branch release.


### Mitigations


See [Security Updates](#security-updates) for the version to install.


### Get the Most Up to Date Product Security Information


Visit the  [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:-----------------|:--------------------------------------------------------------------------------------|
| 3 | January 21, 2022 | Updated the description, base score, and CVSS vector for CVE‑2021‑1113 |
| 2 | January 18, 2022 | Updated the CVSS score and vector for CVE‑2021‑1106, CVE‑2021‑1107, and CVE‑2021‑1108 |
| 1 | August 4, 2021 | Initial release |
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


* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - June 2021](/app/answers/detail/a_id/5205/related/1)
* [ NVIDIA Jetson AGX Xavier, TX1, TX2, and Nano L4T - July 2020](/app/answers/detail/a_id/5039/related/1)
* [ NVIDIA GPU Display Driver - April 2021](/app/answers/detail/a_id/5172/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - March 2022](/app/answers/detail/a_id/5321/related/1)
* [ NVIDIA GeForce Experience - April 2021](/app/answers/detail/a_id/5184/related/1)








