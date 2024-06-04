Security Bulletin: Triton Inference Server - May 2024

**Answer ID: 5546**

NVIDIA has released a software update for NVIDIA Triton Inference Server
to address the issues disclosed in this bulletin. To protect your
system, install the latest release from the [[Triton Inference Server
Releases]{.underline}](https://github.com/triton-inference-server/server/releases)
page on GitHub, and view the [[Secure Deployment Considerations
Guide]{.underline}](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md).

Go to [[NVIDIA Product
Security]{.underline}](https://www.nvidia.com/security/).

### Details

This section provides a summary of the potential vulnerabilities that
this security update addresses and their impact. The descriptions use
[[CWE™]{.underline}](https://cwe.mitre.org/), and base scores and
vectors use [[CVSS
v3.1]{.underline}](https://www.first.org/cvss/v3.1/user-guide)
standards.

+---------+---------+---------+---------+---------+---------+---------+
| **CVE   | *       | **V     | **Base  | **Sev   | **CWE** | **Im    |
| ID**    | *Descri | ector** | Score** | erity** |         | pacts** |
|         | ption** |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| CVE-20  | NVIDIA  | [[AV:N  | 5.4     | Medium  | [[CW    | Info    |
| 24-0103 | Triton  | /AC:L/P |         |         | E-1419] | rmation |
|         | In      | R:L/UI: |         |         | {.under | dis     |
| [[      | ference | N/S:U/C |         |         | line}]( | closure |
| 4607386 | Server  | :L/I:L/ |         |         | https:/ |         |
| ]{.unde | for     | A:N]{.u |         |         | /cwe.mi |         |
| rline}] | Linux   | nderlin |         |         | tre.org |         |
| (https: | and     | e}](htt |         |         | /data/d |         |
| //nvbug | Windows | ps://nv |         |         | efiniti |         |
| spro.nv | c       | d.nist. |         |         | ons/141 |         |
| idia.co | ontains | gov/vul |         |         | 9.html) |         |
| m/bug/4 | a       | n-metri |         |         |         |         |
| 607386) | vulner  | cs/cvss |         |         |         |         |
|         | ability | /v3-cal |         |         |         |         |
| (dupe:  | where a | culator |         |         |         |         |
| 4       | user    | ?vector |         |         |         |         |
| 629688) | may     | =AV:N/A |         |         |         |         |
|         | cause   | C:L/PR: |         |         |         |         |
|         | an      | L/UI:N/ |         |         |         |         |
|         | in      | S:U/C:L |         |         |         |         |
|         | correct | /I:L/A: |         |         |         |         |
|         | initial | N&versi |         |         |         |         |
|         | ization | on=3.1) |         |         |         |         |
|         | of a    |         |         |         |         |         |
|         | r       |         |         |         |         |         |
|         | esource |         |         |         |         |         |
|         | by      |         |         |         |         |         |
|         | network |         |         |         |         |         |
|         | issue.  |         |         |         |         |         |
|         | A       |         |         |         |         |         |
|         | suc     |         |         |         |         |         |
|         | cessful |         |         |         |         |         |
|         | exploit |         |         |         |         |         |
|         | of this |         |         |         |         |         |
|         | vulner  |         |         |         |         |         |
|         | ability |         |         |         |         |         |
|         | may     |         |         |         |         |         |
|         | lead to |         |         |         |         |         |
|         | info    |         |         |         |         |         |
|         | rmation |         |         |         |         |         |
|         | disc    |         |         |         |         |         |
|         | losure. |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| CVE-20  | NVIDIA  | [[AV:N  | 4.3     | Medium  | [[      | Data    |
| 24-0095 | Triton  | /AC:L/P |         |         | CWE-117 | ta      |
|         | In      | R:L/UI: |         |         | ]{.unde | mpering |
| [[      | ference | N/S:U/C |         |         | rline}] |         |
| 4492806 | Server  | :N/I:L/ |         |         | (https: |         |
| ]{.unde | for     | A:N]{.u |         |         | //cwe.m |         |
| rline}] | Linux   | nderlin |         |         | itre.or |         |
| (https: | and     | e}](htt |         |         | g/data/ |         |
| //nvbug | Windows | ps://nv |         |         | definit |         |
| spro.nv | c       | d.nist. |         |         | ions/11 |         |
| idia.co | ontains | gov/vul |         |         | 7.html) |         |
| m/bug/4 | a       | n-metri |         |         |         |         |
| 492806) | vulner  | cs/cvss |         |         |         |         |
|         | ability | /v3-cal |         |         |         |         |
|         | where a | culator |         |         |         |         |
|         | user    | ?vector |         |         |         |         |
|         | can     | =AV:N/A |         |         |         |         |
|         | inject  | C:L/PR: |         |         |         |         |
|         | forged  | L/UI:N/ |         |         |         |         |
|         | logs    | S:U/C:N |         |         |         |         |
|         | and     | /I:L/A: |         |         |         |         |
|         | exe     | N&versi |         |         |         |         |
|         | cutable | on=3.1) |         |         |         |         |
|         | c       |         |         |         |         |         |
|         | ommands |         |         |         |         |         |
|         | by      |         |         |         |         |         |
|         | in      |         |         |         |         |         |
|         | jecting |         |         |         |         |         |
|         | ar      |         |         |         |         |         |
|         | bitrary |         |         |         |         |         |
|         | data as |         |         |         |         |         |
|         | a new   |         |         |         |         |         |
|         | log     |         |         |         |         |         |
|         | entry.  |         |         |         |         |         |
|         | A       |         |         |         |         |         |
|         | suc     |         |         |         |         |         |
|         | cessful |         |         |         |         |         |
|         | exploit |         |         |         |         |         |
|         | of this |         |         |         |         |         |
|         | vulner  |         |         |         |         |         |
|         | ability |         |         |         |         |         |
|         | might   |         |         |         |         |         |
|         | lead to |         |         |         |         |         |
|         | data    |         |         |         |         |         |
|         | tam     |         |         |         |         |         |
|         | pering. |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+

The NVIDIA risk assessment is based on an average of risk across a
diverse set of installed systems and may not represent the true risk to
your local installation. NVIDIA recommends consulting a security or IT
professional to evaluate the risk to your specific configuration.

### Security Updates

The following table lists the NVIDIA software products affected,
versions affected, and the updated version that includes this security
update.

+-------------+-------------+-------------+-------------+-------------+
| **CVE IDs   | **Affected  | **Platform  | **Affected  | **Updated   |
| Addressed** | Products**  | or OS**     | Versions**  | Version**   |
+-------------+-------------+-------------+-------------+-------------+
| CV          | NVIDIA      | Linux,      | 20.10 to    | 24.05       |
| E-2024-0095 | Triton      | Windows     | 24.04       |             |
|             | Inference   |             |             |             |
| [[4492806]  | Server      |             |             |             |
| {.underline |             |             |             |             |
| }](https:// |             |             |             |             |
| nvbugspro.n |             |             |             |             |
| vidia.com/b |             |             |             |             |
| ug/4492806) |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| CV          | NVIDIA      | Linux,      | 23.10 to    | 24.05       |
| E-2024-0103 | Triton      | Windows     | 24.04       |             |
|             | Inference   |             |             |             |
| [[4607386]  | Server      |             |             |             |
| {.underline |             |             |             |             |
| }](https:// |             |             |             |             |
| nvbugspro.n |             |             |             |             |
| vidia.com/b |             |             |             |             |
| ug/4607386) |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

### 

#### Notes

-   Users deploying NVIDIA Triton Inference Server in production
    settings should follow the [[Secure Deployment Considerations
    Guide]{.underline}](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md)
    and ensure that logging and shared memory APIs are protected for use
    by authorized users.

### Acknowledgements

NVIDIA thanks the following individuals for reporting these issues:

CVE-2024-0095: pinkdraconian

CVE-2024-0103: Andrew Innes, Will Williams, Jamie Dougherty, Markus
Hennerbichler

### Get the Most Up-to-Date Product Security Information

Visit the [[NVIDIA Product
Security]{.underline}](https://www.nvidia.com/security) page to

-   Subscribe to security bulletin notifications

-   See the current list of NVIDIA security bulletins

-   Report a potential security issue in any NVIDIA supported product

-   Learn more about the vulnerability management process followed by
    the NVIDIA Product Security Incident Response Team (PSIRT)

### Revision History

  -------------- -------------- -----------------
  **Revision**   **Date**       **Description**
  1.0            May 24, 2024   Initial release
  -------------- -------------- -----------------

### Support

If you have any questions about this security bulletin, contact [[NVIDIA
Support]{.underline}](https://www.nvidia.com/object/support.html).

##### **Disclaimer**

ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES,
DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND
SEPARATELY, "MATERIALS") ARE BEING PROVIDED "AS IS." NVIDIA MAKES NO
WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO
THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS
AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE,
MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE
AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT
PERMITTED BY LAW.

Information is believed to be accurate and reliable at the time it is
furnished. However, NVIDIA Corporation assumes no responsibility for the
consequences of use of such information or for any infringement of
patents or other rights of third parties that may result from its use.
No license is granted by implication or otherwise under any patent or
patent rights of NVIDIA Corporation. Specifications mentioned in this
publication are subject to change without notice. This publication
supersedes and replaces all information previously supplied. NVIDIA
Corporation products are not authorized for use as critical components
in life support devices or systems without express written approval of
NVIDIA Corporation.
