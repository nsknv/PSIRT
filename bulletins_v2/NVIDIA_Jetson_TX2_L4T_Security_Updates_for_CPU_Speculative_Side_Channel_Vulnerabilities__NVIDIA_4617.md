

 NVIDIA Jetson TX2 L4T Security Updates for CPU Speculative Side Channel Vulnerabilities
==========================================================================================================




 Updated 09/29/2021 01:08 PM



Jetson L4T response to CPU speculative side channel vulnerabilities - CVE-2017-5753, CVE-2017-5715, CVE-2017-5754
-----------------------------------------------------------------------------------------------------------------






---




### Bulletin Summary


NVIDIA is providing an initial security update to mitigate aspects of Google Project Zero's January 3, 2018, publication of novel information disclosure attacks that combine CPU speculative execution with known side channels.


NVIDIA believes Jetson TX2 GPU hardware is immune to the reported security issue. Jetson TX2 integrates Arm-based (CPU) processors that may, in certain circumstances, benefit from software mitigations to reduce the risk of the exploits identified in the Google Project Zero disclosure. For more information, refer to the [Arm Security Update](https://developer.arm.com/support/security-update).


This bulletin addresses NVIDIA software updates for Jetson TX2 to mitigate aspects of the potential CPU vulnerabilities.


These potential vulnerabilities have three known variants:


* **Variant 1 (CVE-2017-5753)**: Software mitigations for the Arm CPU issue are provided with the security update included in this bulletin. NVIDIA expects to work together with its ecosystem partners as future updates are released to further strengthen mitigations for the potentially affected CPU.
* **Variant 2 (CVE-2017-5715)**: Software mitigations for the Arm CPU issue are provided with the security update included in this bulletin. NVIDIA expects to work together with its ecosystem partners as future updates are released to further strengthen mitigations for the potentially affected CPU.
* **Variant 3 (CVE-2017-5754)**: NVIDIA believes that Jetson TX2 is not vulnerable to this variant.
* **Variant 3a (CVE-2017-5754)**: Based on [Arm's Security Update](https://developer.arm.com/support/security-update), NVIDIA has no reason to believe that Jetson TX2 needs software mitigations for this variant.


For updates and additional information, actively monitor the [NVIDIA Product Security](https://www.nvidia.com/product-security) page.


### Vulnerability Details


The following sections summarize the potential vulnerabilities. Descriptions are as published on [MITRE](https://cwe.mitre.org/) and risk assessments follow [CVSS](https://www.first.org/cvss/user-guide).


#### CVE-2017-5753


Computer systems with microprocessors utilizing speculative execution and branch prediction may allow unauthorized disclosure of information to unauthorized code with local user access via a side-channel analysis.


CVSS Base Score: 8.2 
CVSS Vector: CVSS:3.0/[AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N)


#### CVE-2017-5715


Computer systems with microprocessors utilizing speculative execution and indirect branch prediction may allow unauthorized disclosure of information to unauthorized code with local user access via a side-channel analysis.


CVSS Base Score: 8.2 
CVSS Vector: CVSS:3.0/[AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N)


#### CVE-2017-5754


Computer systems with microprocessors utilizing speculative execution may allow unauthorized disclosure of information to unauthorized code with local user access via a side-channel analysis of the data cache.


CVSS Base Score: 7.9 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N)


*NVIDIA's risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk of your specific configuration. NVIDIA doesn't know of any exploits to these issues at this time.*


### Updated Products




Updated Products
| \*\*Product\*\* | \*\*Integrated CPU\*\* | \*\*OS\*\* |
| --- | --- | --- |
| Jetson TX2 | \* Arm Cortex-A57 processor \* Armv8-A NVIDIA processor | Linux for Tegra |


### Security Updates


When available, download updates from [*NVIDIA DevZone*](https://developer.nvidia.com/embedded/downloads).




Security Updates
| \*\*Product Series\*\* | \*\*OS\*\* | \*\*Updated Version\*\* |
| --- | --- | --- |
| Jetson TX2 | Linux for Tegra | BSP 28.2 |


### Acknowledgements


None.


### Get the Most Up to Date Product Security Information


To learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT), see the current list of NVIDIA security bulletins, or subscribe to security bulletin notifications, go to [NVIDIA Product Security](http://www.nvidia.com/product-security).


### Revision History




Revision History




| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 5.0 | March 13, 2018 | Revised the Security Updates table with the availability of the updated version |
| 4.0 | March 1, 2018 | Revised the expected availability of the updated version |
| 3.0 | February 6, 2018 | Revised the expected availability of the updated version |
| 2.0 | January 16, 2018 | Clarified affected Arm CPU components |
| 1.0 | January 5, 2018 | Initial release |


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA Driver Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4611/related/1)
* [ NVIDIA SHIELD TV Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4613/related/1)
* [Security Notice: CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4609/related/1)
* [ NVIDIA Jetson TX1, Jetson TK1, and Tegra K1 L4T Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4616/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - June 2023](/app/answers/detail/a_id/5466/related/1)








