# NVIDIA CUDA Toolkit (Bulletin ID: 5373)



 NVIDIA CUDA Toolkit - October 2022
=====================================================




 Updated 10/05/2022 03:24 PM



NVIDIA has released a software update for NVIDIA® CUDA® Toolkit software. This update addresses security issues that may lead to code execution, denial of service, or information disclosure.


To protect your system, download and install this software update from the [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-toolkit) page.


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/specification-document) standards.




| \*\*CVE ID\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector\*\* |
| --- | --- | --- | --- |
| CVE‑2022‑34667 | NVIDIA CUDA Toolkit SDK contains a stack-based buffer overflow vulnerability in `cuobjdump`, where an unprivileged remote attacker could exploit this buffer overflow condition by persuading a local user to download a specially crafted corrupted file and execute `cuobjdump` against it locally, which may lead to a limited denial of service and some loss of data integrity for the local user. | 4.4 | [AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:L) |


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends evaluating the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update.


Download the update from the [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-toolkit) page to apply the security update.




| CVE IDs Addressed | Software Product | Operating System | Affected Versions | Updated Version |
| --- | --- | --- | --- | --- |
| CVE‑2022‑34667 | NVIDIA CUDA Toolkit | Linux and Windows | All versions prior to 11.8 | 11.8 |


#### Notes


* Earlier software releases of this product are also affected. If you are using an earlier release, upgrade to the latest release.


### Acknowledgements


CVE‑2022‑34667: NVIDIA thanks hjy79425575 for reporting this issue.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History








| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 1.0 | October 5, 2022 | Initial release |


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


* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - March 2022](/app/answers/detail/a_id/5321/related/1)
* [ NVIDIA GPU Display Driver - May 2022](/app/answers/detail/a_id/5353/related/1)
* [ NVIDIA Omniverse Nucleus and Omniverse Cache - April 2022](/app/answers/detail/a_id/5342/related/1)
* [Security Notice: NVIDIA Response to Security Incident - March 2022](/app/answers/detail/a_id/5333/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX) - April 2022](/app/answers/detail/a_id/5343/related/1)








