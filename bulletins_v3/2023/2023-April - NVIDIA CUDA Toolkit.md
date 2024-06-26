# NVIDIA CUDA Toolkit (Bulletin ID: 5456)



 NVIDIA CUDA Toolkit - April 2023
===================================================




 Updated 04/21/2023 09:09 AM



NVIDIA has released a software update for NVIDIA® CUDA® Toolkit software. This update addresses security issues that may lead to code execution, limited denial of service, and limited information disclosure.


To protect your system, download and install this software update from the [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-toolkit) page.


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section summarizes the potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors follow [CVSS v3.1](https://www.first.org/cvss/user-guide) standards.




| \*\*CVE ID\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector and CWE\*\* |
| --- | --- | --- | --- |
| CVE‑2023‑25512 | NVIDIA CUDA toolkit for Linux and Windows contains a vulnerability in `cuobjdump`, where an attacker may cause an out-of-bounds memory read by running `cuobjdump` on a malformed input file. A successful exploit of this vulnerability may lead to limited denial of service, code execution, and limited information disclosure. | 5.3 | [AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L&version=3.1) [CWE‑125](https://cwe.mitre.org/data/definitions/125.html) |
| CVE‑2023‑25513 | NVIDIA CUDA toolkit for Linux and Windows contains a vulnerability in `cuobjdump`, where an attacker may cause an out-of-bounds read by tricking a user into running `cuobjdump` on a malformed input file. A successful exploit of this vulnerability may lead to limited denial of service, code execution, and limited information disclosure. | 5.3 | [AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L) [CWE‑125](https://cwe.mitre.org/data/definitions/125.html) |
| CVE‑2023‑25514 | NVIDIA CUDA toolkit for Linux and Windows contains a vulnerability in `cuobjdump`, where an attacker may cause an out-of-bounds read by tricking a user into running `cuobjdump` on a malformed input file. A successful exploit of this vulnerability may lead to limited denial of service, code execution, and limited information disclosure. | 5.3 | [AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L) [CWE‑125](https://cwe.mitre.org/data/definitions/125.html) |
| CVE‑2023‑25510 | NVIDIA CUDA Toolkit SDK for Linux and Windows contains a NULL pointer dereference in `cuobjdump`, where a local user running the tool against a malformed binary may cause a limited denial of service. | 3.3 | [AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L) [CWE‑476](https://cwe.mitre.org/data/definitions/476.html) |
| CVE‑2023‑25511 | NVIDIA CUDA Toolkit for Linux and Windows contains a vulnerability in `cuobjdump`, where a division-by-zero error may enable a user to cause a crash, which may lead to a limited denial of service. | 3.3 | [AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L) [CWE‑369](https://cwe.mitre.org/data/definitions/369.html) |


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends evaluating the risk to your specific configuration.


### Security Updates


The following table lists the software products and versions affected, and the updated version available from nvidia.com that includes this security update.


Download the update from the [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-toolkit) page to apply the security update.




| \*\*CVEs Addressed\*\* | \*\*Software Product\*\* | \*\*Operating System\*\* | \*\*Affected Versions\*\* | \*\*Updated Version\*\* |
| --- | --- | --- | --- | --- |
| CVE‑2023‑25510 CVE‑2023‑25511 CVE‑2023‑25514 | NVIDIA CUDA Toolkit | Linux, Windows | All versions prior to 12.1 Update 1 | 12.1 Update 1 |
| CVE‑2023‑25512 | NVIDIA CUDA Toolkit | Linux, Windows | All versions prior to 12.1 | 12.1 |
| CVE‑2023‑25513 | NVIDIA CUDA Toolkit | Linux, Windows | All versions prior to 12.0 Update 1 | 12.0 Update 1 |


#### Notes


* Earlier software releases of this product are also affected. If you are using an earlier release, upgrade to the latest release version.


### Acknowledgements


NVIDIA thanks the following people for reporting these issues:


* CVE‑2023‑25510, CVE‑2023‑25511: zz zr, Zhaozixi105
* CVE‑2023‑25512: Luca Di Bartolomeo @ EPFL, Zhaozixi105
* CVE‑2023‑25513: Luca Di Bartolomeo @ EPFL


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History








| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 1.0 | April 21, 2023 | Initial release |


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


* [ NVIDIA GPU Display Driver - March 2023](/app/answers/detail/a_id/5452/related/1)
* [ NVIDIA CUDA Toolkit - March 2023](/app/answers/detail/a_id/5446/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series - January 2023](/app/answers/detail/a_id/5442/related/1)
* [ NVIDIA GeForce Experience - January 2023](/app/answers/detail/a_id/5384/related/1)
* [Security Notice: NVIDIA Response to OpenSSL Vulnerabilities - November 2022](/app/answers/detail/a_id/5405/related/1)








