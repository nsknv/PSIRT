

 NVIDIA GeForce Experience (GFE) Security Updates for CPU Speculative Side Channel Vulnerabilities
====================================================================================================================




 Updated 09/29/2021 01:08 PM



NVIDIA GeForce Experience (GFE) response to CPU speculative side channel vulnerabilities - CVE-2017-5753, CVE-2017-5715, CVE-2017-5754
--------------------------------------------------------------------------------------------------------------------------------------






---




### Bulletin Summary


NVIDIA is providing an initial security update to mitigate aspects of Google Project Zero's January 3, 2018 publication of novel information disclosure attacks that combine CPU speculative execution with known side channels.


NVIDIA's core business is GPU computing.


**NVIDIA believes our GPU hardware is immune to the reported security issue. As for our driver software, we are providing updates to help mitigate the CPU security issue. You can find information about the driver software updates in [Security Bulletin 4611](http://nvidia.custhelp.com/app/answers/detail/a_id/4611).**


This bulletin addresses updates for NVIDIA GeForce Experience (GFE) software to help mitigate potential CPU security vulnerabilities.


The potential vulnerabilities have three known variants:


* **Variant 1 (CVE-2017-5753)**: Software mitigations for the CPU issue are provided with the security update included in this bulletin. NVIDIA expects to work together with its ecosystem partners as future updates are released to further strengthen mitigations for the potentially affected CPUs.
* **Variant 2 (CVE-2017-5715)**: NVIDIA's initial analysis indicates that GFE running on potentially affected CPUs may require further updates. NVIDIA expects to work together with its ecosystem partners as they release future updates for this variant.
* **Variant 3 (CVE-2017-5754)**: NVIDIA believes that GFE is not vulnerable to this variant.


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


*NVIDIA's risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk of your specific configuration.*


### Updated Products


| Product | Operating System |
|:----------------------------------|:-------------------|
| GeForce Experience (GFE) Software | Windows |
### Security Updates


When the update is available, it will be automatically applied by the OTA update. You can also download the update from the [NVIDIA GeForce Experience Download](http://www.geforce.com/geforce-experience/download) page.


| Product Series | Updated Version |
|:-----------------------|:------------------|
| GeForce Experience 3.x | 3.12.0.84 |
**Note:** If you are using an earlier product series of GFE, upgrade to a supported series that contains the update as listed in the Security Updates table.


### Acknowledgements


None.


### Revision History


| Revision | Date | Description |
|-----------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| 3 | January 18, 2018 | Updated information about available security updates |
| 2 | January 16, 2018 | Added clarification that GPU hardware is not affected and that NVIDIA is updating its drivers to help mitigate the CPU security issue |
| 1 | January 9, 2018 | Initial release |
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
* [Security Notice: CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4609/related/1)
* [ NVIDIA SHIELD TV Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4613/related/1)
* [ NVIDIA Jetson TX1, Jetson TK1, and Tegra K1 L4T Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4616/related/1)
* [ NVIDIA Jetson TX2 L4T Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4617/related/1)








