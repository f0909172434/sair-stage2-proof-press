# Exact upstream license texts are embedded below and hash-bound by tests.
# Copyright 2026 SAIR Foundation
# Copyright 2025 Contributors of the Equational Theories Project
# Modified in 2026 for this competition submission: deterministic proof and
# countermodel search, generated ID-free magma catalog, and portfolio evidence.

"""Deterministic SAIR Stage 2 Solo solver.

This submission is adapted from the official SAIR Solo ``baseline`` and
``opnorm`` examples, inspected at official repository commit
2848228ff490422442878fd6f5abaf4cfa95257d:

https://github.com/SAIRcompetition/equational-theories-lean-stage2

The implementation below is deliberately self-contained and uses only the
Python standard library.  It never opens a network connection or reads an
auxiliary file.  Its only external interfaces are the organizer proxy's
newline-delimited JSON messages on stdin/stdout.  LLM use, when reached, is
requested only through that proxy; this file contains no API client or key.
"""

SAIR_UPSTREAM_LICENSE = r"""
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for describing the origin of the Work and
      reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Support. While redistributing the Work or
      Derivative Works thereof, You may choose to offer, and charge a
      fee for, acceptance of support, warranty, indemnity, or other
      liability obligations and/or rights consistent with this License.
      However, in accepting such obligations, You may act only on Your
      own behalf and on Your sole responsibility, not on behalf of any
      other Contributor, and only if You agree to indemnify, defend, and
      hold each Contributor harmless for any liability incurred by, or
      claims asserted against, such Contributor by reason of Your
      accepting any such warranty or support.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2026 SAIR Foundation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
   implied. See the License for the specific language governing permissions
   and limitations under the License.
"""

EQT_UPSTREAM_LICENSE = r"""
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2025 Contributors of the Equational Theories Project

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

PROMPT = 'Propose short bridge equations for one universal implication in an arbitrary magma. Your output is untrusted search advice. A local deterministic controller will independently parse every term, reconstruct every adjacent implication, replay every proof from the exact hypothesis, compose the certificate, and let pinned Lean decide acceptance. Never decide whether the implication is true or false. Never return a verdict, proof, Lean text, code, certificate, countermodel, row identifier, label, explanation, commentary, or Markdown.\n\nHypothesis ({problem.eq1_name}): {problem.equation1}\nGoal ({problem.eq2_name}): {problem.equation2}\n\nRound: {solver.round} of 3\nMode: {solver.mode}\nFrozen deterministic-search summary:\n{solver.deterministic_trace_summary}\nTyped aggregate feedback from the preceding response:\n{solver.protocol_feedback}\nPreviously tried bounded plans: {solver.tried_plan_count}\n\nOutput 1 to 4 consecutive JSON objects, one object per line, with no surrounding array and no other text. Every object must have exactly this shape and no other keys:\n{"chains":[{"waypoints":[{"left":"x","right":"x * y"}]}]}\n\nSchema limits for each JSON object:\n- `chains` contains 1 to 4 priority-ordered chains.\n- Every chain has the single exact key `waypoints` and contains 1 or 2 equations.\n- Every waypoint has exactly the string keys `left` and `right`.\n- Use lowercase variable names, parentheses, and only the binary magma operator `*` or `◇`.\n- Each side has at most 8 operator occurrences, at most 5 variables, and at most 512 characters.\n- Each object has at most 8 distinct waypoints. Never repeat an equation up to variable renaming or reversal.\n- A waypoint differs from both the displayed hypothesis and goal and never has identical sides.\n\nThe selected controller is fixed and cannot be negotiated:\n- variant `compact_tight`; compact cap tier;\n- engine order on every link: expanded-goal paramodulation first, then demodulating-goal paramodulation;\n- at most 12 total engine invocations across the whole response;\n- at most 8 seconds per engine and 45 seconds for the whole response verification;\n- per engine: depth 12, 512 rules, 2048 candidates, queue 32768, term size 45; demodulation performs at most 4 rewrites per side;\n- response-local exact-link caching is shared across objects; timeout, cap, deadline, invocation exhaustion, replay failure, or controller exception always abstains.\n\nSpend the finite controller budget on the easiest proof first. Object order, then chain order, then link order is priority. Put the single most promising one-waypoint chain first. A link that the expanded engine proves directly usually costs one invocation; a link requiring the demodulating engine usually costs two. Four unrelated three-link chains can exhaust the budget before later objects are examined. Reuse exact adjacent links across diverse plans only when that genuinely preserves useful alternatives and benefits from the response-local cache.\n\nSearch for H -> W1 -> W2 -> G; the goal is appended locally, so never include the goal as a waypoint. Use these views before ordering plans:\n1. Forward consequence: choose a concise identity obtained from H by a direct substitution or a very short paramodulation.\n2. Backward generalization: choose a slightly more general identity whose direct substitution gives G.\n3. Meet in the middle: use one bridge whenever both links are simple; use two only when all three links become materially easier.\n4. Demodulation opportunity: when a repeated subterm can be reduced using a hypothesis instance, preserve the exact repeated-variable alignment needed for that reduction.\n\nPrefer algebraically meaningful bridges that preserve repeated-variable positions and nesting shared by H and G. Prefer direct instances, shallow terms, and outer shapes already visible in H or G. Avoid cosmetic alpha-renamings, oversized balanced terms, speculative identities, and chains whose first link is harder than the original implication.\n\nUse typed feedback literally in rounds 2 and 3:\n- `forward_link_unproved`: move the first bridge closer to a direct consequence of H.\n- `middle_link_unproved`: replace both bridges or collapse to one; do not merely rename variables.\n- `goal_link_unproved`: make the last bridge a direct generalization or substitution parent of G.\n- `engine_timeout` or `engine_cap_exhausted`: use substantially shallower terms and a more direct substitution.\n- `response_deadline_exhausted` or `engine_invocation_budget_exhausted`: return fewer objects/chains, put the easiest chain first, and share exact links only when useful.\n- parser, schema, term-cap, duplicate, or degenerate feedback: repair that exact constraint.\n- Lean rejection or composition replay failure: choose a structurally different chain rather than repeating the same plan.\n\nEvery later round must be genuinely different from all prior plan digests. Before returning, verify exact JSON syntax, object order, key names, chain and waypoint counts, term caps, controller budget realism, and the absence of every forbidden field or prose.'

from base64 import b85decode
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
import heapq
from itertools import product
import json
import re
import sys
from zlib import decompress


# The order is part of the solver's reproducibility contract.
STRATEGY_ORDER = (
    "reflexive_goal",
    "direct_substitution",
    "singleton_collapse",
    "direct_law_normalization",
    "distilled_right_projection",
    "distilled_left_insensitive",
    "bounded_rewrite",
    "bidirectional_rewrite",
    "fin2_3_exhaustive",
    "fin4_7_structured",
    "fixed_generated_countermodels",
    "public_magma_catalog",
    "large_public_countermodels",
    "dual_number_affine_countermodels",
    "polyhedral_guarded_action_countermodels",
    "dual_reflection_countermodels",
    "goal_directed_paramodulation",
    "symbolic_narrowing",
    "goal_guided_symbolic_beam",
    "late_goal_directed_paramodulation",
    "deep_goal_directed_paramodulation",
    "product_collapse_bridge",
    "extended_goal_directed_paramodulation",
    "deep_goal_guided_symbolic_beam",
    "derived_singleton_paramodulation",
    "organizer_proxy_llm",
)

MAX_REWRITE_DEPTH = 3
MAX_REWRITE_STATES = 700
MAX_BIDIRECTIONAL_DEPTH = 2
MAX_BIDIRECTIONAL_STATES = 1400
MAX_BIDIRECTIONAL_SUCCESSORS = 500
MAX_BIDIRECTIONAL_CHOICES = 192
MAX_BIDIRECTIONAL_TERM_SIZE = 35
MAX_BIDIRECTIONAL_POOL_TERM_SIZE = 17
MAX_SYMBOLIC_STATES = 192
MAX_SYMBOLIC_TERM_SIZE = 35
MAX_SYMBOLIC_SUCCESSORS = 70
MAX_SYMBOLIC_BEAM_DEPTH = 7
MAX_SYMBOLIC_BEAM_WIDTH = 64
MAX_SYMBOLIC_BEAM_TERM_SIZE = 35
MAX_SYMBOLIC_BEAM_SUCCESSORS = 70
MAX_DERIVED_SINGLETON_DEPTH = 7
MAX_DERIVED_SINGLETON_RULES = 64
MAX_DERIVED_SINGLETON_CANDIDATES = 128
MAX_DERIVED_SINGLETON_QUEUE = 2048
MAX_DERIVED_SINGLETON_TERM_SIZE = 9
MAX_GOAL_PARAMOD_DEPTH = 8
MAX_GOAL_PARAMOD_RULES = 48
MAX_GOAL_PARAMOD_CANDIDATES = 48
MAX_GOAL_PARAMOD_QUEUE = 2048
MAX_GOAL_PARAMOD_TERM_SIZE = 11
MAX_LATE_GOAL_PARAMOD_DEPTH = 9
MAX_LATE_GOAL_PARAMOD_RULES = 96
MAX_LATE_GOAL_PARAMOD_CANDIDATES = 128
MAX_LATE_GOAL_PARAMOD_QUEUE = 2048
MAX_LATE_GOAL_PARAMOD_TERM_SIZE = 19
MAX_DEEP_GOAL_PARAMOD_DEPTH = 12
MAX_DEEP_GOAL_PARAMOD_RULES = 256
MAX_DEEP_GOAL_PARAMOD_CANDIDATES = 512
MAX_DEEP_GOAL_PARAMOD_QUEUE = 8192
MAX_DEEP_GOAL_PARAMOD_TERM_SIZE = 23
MAX_EXTENDED_GOAL_PARAMOD_DEPTH = 14
MAX_EXTENDED_GOAL_PARAMOD_RULES = 1024
MAX_EXTENDED_GOAL_PARAMOD_CANDIDATES = 4096
MAX_EXTENDED_GOAL_PARAMOD_QUEUE = 65536
MAX_EXTENDED_GOAL_PARAMOD_TERM_SIZE = 45
DEEP_SYMBOLIC_BEAM_TIERS = (
    (5, 200, 23, 16),
    (8, 256, 55, 256),
)
MAX_LLM_ROUNDS = 3
MAX_LLM_COUNTERMODEL_CARRIER = 8
MAX_INTERNAL_COUNTERMODEL_CARRIER = 13
MAX_STRUCTURAL_COUNTERMODEL_CASES = 1024
MAX_STRUCTURAL_FALSE_CERT_BYTES = 10_000

# These three tables were generated from the official public/development
# corpora by deterministic bounded searches, independently rechecked, and
# accepted twice by the official local Lean judge.  Their exact provenance and
# canonical SHA-256 digests are recorded in the portfolio evidence.  The
# submission embeds the tiny results, not the exploratory runtime search.
FIXED_GENERATED_COUNTERMODEL_TABLES = (
    (
        4,
        (
            (0, 1, 2, 3),
            (0, 0, 0, 3),
            (0, 3, 0, 3),
            (0, 1, 2, 0),
        ),
    ),
    (
        5,
        (
            (0, 0, 4, 1, 2),
            (3, 2, 1, 2, 4),
            (3, 1, 2, 4, 3),
            (0, 4, 0, 3, 0),
            (3, 0, 4, 2, 1),
        ),
    ),
    (
        8,
        (
            (0, 7, 5, 2, 1, 6, 4, 3),
            (2, 5, 7, 0, 3, 4, 6, 1),
            (4, 3, 1, 6, 5, 2, 0, 7),
            (6, 1, 3, 4, 7, 0, 2, 5),
            (3, 4, 6, 1, 2, 5, 7, 0),
            (1, 6, 4, 3, 0, 7, 5, 2),
            (7, 0, 2, 5, 6, 1, 3, 4),
            (5, 2, 0, 7, 4, 3, 1, 6),
        ),
    ),
)

# These two larger public finite models come from the Equational Theories
# Project global coverage plan at commit 54edcda2f320cef0a241f8109fa164f901a69b87
# (Apache-2.0).  The tables are stored without equation IDs or answer maps and
# were independently checked by complete assignment enumeration.  Because the
# compact public ``finOpTable`` parser is digit-based, carriers above Fin 8 use
# a structural inductive carrier and exhaustive kernel-checked ``cases`` proof.
LARGE_PUBLIC_COUNTERMODEL_TABLES = (
    (
        9,
        (
            (1, 2, 4, 8, 3, 0, 7, 5, 6),
            (7, 5, 0, 2, 1, 6, 3, 8, 4),
            (3, 8, 6, 5, 7, 4, 1, 2, 0),
            (7, 5, 0, 2, 1, 6, 3, 8, 4),
            (1, 2, 4, 8, 3, 0, 7, 5, 6),
            (3, 8, 6, 5, 7, 4, 1, 2, 0),
            (1, 2, 4, 8, 3, 0, 7, 5, 6),
            (7, 5, 0, 2, 1, 6, 3, 8, 4),
            (3, 8, 6, 5, 7, 4, 1, 2, 0),
        ),
    ),
    (
        13,
        (
            (0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1),
            (2, 1, 11, 7, 9, 4, 8, 0, 3, 12, 6, 5, 10),
            (3, 11, 2, 12, 8, 10, 5, 9, 0, 4, 1, 7, 6),
            (4, 7, 12, 3, 1, 9, 11, 6, 10, 0, 5, 2, 8),
            (5, 9, 8, 1, 4, 2, 10, 12, 7, 11, 0, 6, 3),
            (6, 4, 10, 9, 2, 5, 3, 11, 1, 8, 12, 0, 7),
            (7, 8, 5, 11, 10, 3, 6, 4, 12, 2, 9, 1, 0),
            (8, 0, 9, 6, 12, 11, 4, 7, 5, 1, 3, 10, 2),
            (9, 3, 0, 10, 7, 1, 12, 5, 8, 6, 2, 4, 11),
            (10, 12, 4, 0, 11, 8, 2, 1, 6, 9, 7, 3, 5),
            (11, 6, 1, 5, 0, 12, 9, 3, 2, 7, 10, 8, 4),
            (12, 5, 7, 2, 6, 0, 1, 10, 4, 3, 8, 11, 9),
            (1, 10, 6, 8, 3, 7, 0, 2, 11, 5, 4, 9, 12),
        ),
    ),
)

# The following ID-free catalog is generated from the global finite-magma
# coverage plan in teorth/equational_theories at commit 54edcda2f320cef0...
# (Apache-2.0).  Generation discards equation IDs and Satisfies/Refutes maps,
# exact-deduplicates Fin 4--8 tables, and removes Candidate 5 duplicates.  The
# submission note records the full source, builder, hashes, and reproduction.
# BEGIN GENERATED PUBLIC MAGMA CATALOG
PUBLIC_MAGMA_CATALOG = (
    (7, ((0, 2, 1, 4, 3, 6, 5), (3, 1, 5, 0, 6, 2, 4), (4, 6, 2, 5, 0, 3, 1), (6, 5, 4, 3, 2, 1, 0), (5, 3, 6, 1, 4, 0, 2), (2, 4, 0, 6, 1, 5, 3), (1, 0, 3, 2, 5, 4, 6))),
    (7, ((0, 2, 3, 1, 5, 6, 4), (4, 1, 6, 0, 3, 2, 5), (5, 0, 2, 4, 6, 1, 3), (6, 5, 0, 3, 1, 4, 2), (1, 6, 5, 2, 4, 3, 0), (2, 3, 4, 6, 0, 5, 1), (3, 4, 1, 5, 2, 0, 6))),
    (7, ((0, 2, 3, 4, 5, 6, 1), (6, 1, 0, 5, 2, 4, 3), (1, 4, 2, 0, 6, 3, 5), (2, 6, 5, 3, 0, 1, 4), (3, 5, 1, 6, 4, 0, 2), (4, 3, 6, 2, 1, 5, 0), (5, 0, 4, 1, 3, 2, 6))),
    (7, ((0, 2, 3, 4, 5, 6, 1), (6, 1, 0, 5, 3, 2, 4), (1, 5, 2, 0, 6, 4, 3), (2, 4, 6, 3, 0, 1, 5), (3, 6, 5, 1, 4, 0, 2), (4, 3, 1, 6, 2, 5, 0), (5, 0, 4, 2, 1, 3, 6))),
    (8, ((0, 2, 3, 4, 5, 6, 7, 1), (4, 1, 6, 0, 7, 3, 5, 2), (5, 3, 2, 7, 0, 1, 4, 6), (6, 7, 4, 3, 1, 0, 2, 5), (7, 6, 1, 5, 4, 2, 0, 3), (1, 4, 7, 2, 6, 5, 3, 0), (2, 0, 5, 1, 3, 7, 6, 4), (3, 5, 0, 6, 2, 4, 1, 7))),
    (8, ((0, 2, 3, 4, 5, 6, 7, 1), (6, 1, 5, 7, 3, 0, 4, 2), (7, 3, 2, 6, 1, 4, 0, 5), (1, 6, 4, 3, 7, 2, 5, 0), (2, 0, 7, 5, 4, 1, 3, 6), (3, 7, 0, 1, 6, 5, 2, 4), (4, 5, 1, 0, 2, 7, 6, 3), (5, 4, 6, 2, 0, 3, 1, 7))),
    (8, ((0, 3, 4, 6, 1, 2, 7, 5), (4, 2, 0, 1, 6, 3, 5, 7), (5, 6, 7, 3, 2, 1, 4, 0), (1, 7, 6, 4, 0, 5, 3, 2), (2, 4, 3, 7, 5, 0, 6, 1), (7, 1, 5, 2, 3, 6, 0, 4), (3, 0, 2, 5, 7, 4, 1, 6), (6, 5, 1, 0, 4, 7, 2, 3))),
    (6, ((1, 2, 3, 0, 5, 4), (2, 1, 4, 5, 0, 3), (5, 4, 1, 2, 3, 0), (4, 5, 0, 3, 2, 1), (3, 0, 5, 4, 1, 2), (0, 3, 2, 1, 4, 5))),
    (6, ((1, 2, 3, 4, 5, 0), (4, 1, 2, 5, 0, 3), (3, 0, 5, 2, 1, 4), (0, 5, 4, 3, 2, 1), (5, 4, 1, 0, 3, 2), (2, 3, 0, 1, 4, 5))),
    (7, ((1, 2, 4, 0, 6, 5, 3), (4, 3, 1, 5, 2, 0, 6), (0, 6, 5, 1, 3, 4, 2), (5, 0, 6, 2, 4, 3, 1), (3, 4, 2, 6, 0, 1, 5), (2, 1, 3, 4, 5, 6, 0), (6, 5, 0, 3, 1, 2, 4))),
    (7, ((1, 2, 3, 4, 5, 0, 6), (4, 1, 6, 5, 3, 2, 0), (6, 3, 1, 0, 2, 5, 4), (2, 0, 5, 1, 4, 6, 3), (0, 6, 4, 2, 1, 3, 5), (5, 4, 0, 3, 6, 1, 2), (3, 5, 2, 6, 0, 4, 1))),
    (7, ((0, 1, 2, 3, 4, 5, 6), (2, 3, 1, 4, 5, 6, 0), (4, 6, 5, 0, 2, 1, 3), (5, 0, 6, 2, 1, 3, 4), (1, 4, 3, 5, 6, 0, 2), (6, 2, 0, 1, 3, 4, 5), (3, 5, 4, 6, 0, 2, 1))),
    (7, ((0, 2, 3, 1, 6, 4, 5), (1, 4, 5, 2, 0, 3, 6), (2, 3, 6, 4, 1, 5, 0), (3, 6, 1, 5, 4, 0, 2), (4, 5, 0, 3, 2, 6, 1), (5, 0, 2, 6, 3, 1, 4), (6, 1, 4, 0, 5, 2, 3))),
    (7, ((1, 2, 0, 3, 6, 4, 5), (3, 1, 6, 5, 2, 0, 4), (4, 5, 1, 0, 3, 2, 6), (2, 6, 4, 1, 0, 5, 3), (5, 3, 2, 4, 1, 6, 0), (0, 4, 3, 6, 5, 1, 2), (6, 0, 5, 2, 4, 3, 1))),
    (7, ((1, 2, 3, 4, 5, 0, 6), (6, 3, 0, 2, 1, 5, 4), (5, 4, 2, 6, 0, 3, 1), (2, 5, 1, 0, 4, 6, 3), (4, 0, 5, 3, 6, 1, 2), (3, 1, 6, 5, 2, 4, 0), (0, 6, 4, 1, 3, 2, 5))),
    (7, ((1, 2, 3, 4, 5, 0, 6), (3, 1, 6, 5, 2, 4, 0), (2, 5, 1, 0, 4, 6, 3), (0, 6, 4, 1, 3, 2, 5), (6, 3, 0, 2, 1, 5, 4), (4, 0, 5, 3, 6, 1, 2), (5, 4, 2, 6, 0, 3, 1))),
    (7, ((1, 2, 3, 4, 5, 0, 6), (5, 4, 0, 3, 6, 1, 2), (4, 1, 6, 5, 3, 2, 0), (0, 6, 4, 2, 1, 3, 5), (3, 5, 2, 6, 0, 4, 1), (6, 3, 1, 0, 2, 5, 4), (2, 0, 5, 1, 4, 6, 3))),
    (7, ((1, 2, 0, 6, 4, 3, 5), (4, 3, 1, 2, 5, 0, 6), (3, 5, 2, 4, 0, 6, 1), (0, 6, 3, 5, 1, 2, 4), (5, 0, 4, 3, 6, 1, 2), (6, 1, 5, 0, 2, 4, 3), (2, 4, 6, 1, 3, 5, 0))),
    (7, ((1, 2, 0, 3, 6, 4, 5), (4, 1, 6, 2, 5, 0, 3), (3, 5, 1, 6, 4, 2, 0), (0, 4, 5, 1, 3, 6, 2), (5, 6, 2, 0, 1, 3, 4), (2, 3, 4, 5, 0, 1, 6), (6, 0, 3, 4, 2, 5, 1))),
    (8, ((1, 2, 3, 4, 5, 6, 7, 0), (6, 3, 4, 5, 2, 7, 0, 1), (7, 0, 5, 6, 3, 4, 1, 2), (4, 5, 6, 3, 0, 1, 2, 7), (5, 6, 7, 0, 1, 2, 3, 4), (2, 7, 0, 1, 6, 3, 4, 5), (3, 4, 1, 2, 7, 0, 5, 6), (0, 1, 2, 7, 4, 5, 6, 3))),
    (8, ((1, 2, 3, 0, 6, 7, 4, 5), (4, 3, 5, 1, 2, 0, 6, 7), (3, 0, 1, 2, 7, 6, 5, 4), (5, 1, 4, 3, 0, 2, 7, 6), (6, 5, 7, 4, 1, 3, 0, 2), (7, 4, 6, 5, 3, 1, 2, 0), (2, 7, 0, 6, 4, 5, 3, 1), (0, 6, 2, 7, 5, 4, 1, 3))),
    (8, ((1, 2, 4, 0, 5, 6, 3, 7), (7, 3, 5, 6, 4, 0, 2, 1), (2, 1, 6, 5, 0, 4, 7, 3), (6, 4, 2, 7, 3, 1, 5, 0), (0, 5, 3, 1, 2, 7, 4, 6), (3, 7, 0, 4, 6, 5, 1, 2), (4, 6, 1, 3, 7, 2, 0, 5), (5, 0, 7, 2, 1, 3, 6, 4))),
    (8, ((1, 2, 5, 6, 4, 3, 7, 0), (4, 3, 0, 7, 1, 2, 6, 5), (2, 1, 7, 0, 3, 4, 5, 6), (0, 6, 4, 2, 5, 7, 3, 1), (7, 5, 2, 4, 6, 0, 1, 3), (6, 0, 3, 1, 7, 5, 4, 2), (3, 4, 6, 5, 2, 1, 0, 7), (5, 7, 1, 3, 0, 6, 2, 4))),
    (7, ((1, 2, 3, 4, 5, 0, 6), (5, 3, 2, 0, 1, 6, 4), (6, 5, 0, 2, 4, 3, 1), (0, 4, 6, 5, 2, 1, 3), (4, 0, 1, 3, 6, 2, 5), (2, 1, 5, 6, 3, 4, 0), (3, 6, 4, 1, 0, 5, 2))),
    (7, ((1, 2, 5, 6, 0, 3, 4), (4, 0, 1, 5, 6, 2, 3), (3, 6, 4, 1, 5, 0, 2), (0, 1, 2, 3, 4, 5, 6), (5, 3, 6, 0, 2, 4, 1), (2, 5, 3, 4, 1, 6, 0), (6, 4, 0, 2, 3, 1, 5))),
    (6, ((1, 0, 3, 2, 5, 4), (2, 3, 4, 5, 0, 1), (5, 4, 1, 0, 3, 2), (0, 1, 2, 3, 4, 5), (3, 2, 5, 4, 1, 0), (4, 5, 0, 1, 2, 3))),
    (6, ((1, 2, 3, 4, 5, 0), (0, 5, 4, 3, 2, 1), (5, 4, 1, 0, 3, 2), (4, 1, 2, 5, 0, 3), (3, 0, 5, 2, 1, 4), (2, 3, 0, 1, 4, 5))),
    (7, ((1, 2, 6, 5, 3, 4, 1), (6, 1, 2, 1, 1, 5, 1), (3, 2, 2, 2, 6, 4, 5), (4, 1, 2, 3, 3, 5, 1), (5, 1, 5, 3, 4, 4, 6), (3, 5, 6, 5, 4, 5, 5), (2, 1, 4, 1, 6, 5, 6))),
    (8, ((1, 4, 2, 2, 1, 6, 0, 0), (2, 3, 2, 4, 3, 6, 1, 1), (2, 2, 2, 2, 2, 2, 2, 2), (4, 2, 2, 0, 0, 6, 3, 3), (0, 1, 2, 3, 5, 6, 5, 6), (4, 4, 2, 4, 6, 4, 4, 6), (1, 3, 2, 0, 5, 4, 7, 6), (1, 3, 2, 0, 6, 6, 6, 6))),
    (5, ((0, 2, 3, 0, 0), (4, 1, 4, 4, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3), (4, 4, 4, 4, 4))),
    (4, ((0, 1, 3, 3), (3, 3, 0, 2), (1, 0, 1, 0), (0, 3, 2, 2))),
    (4, ((2, 3, 2, 3), (3, 2, 3, 2), (1, 0, 1, 0), (0, 1, 0, 1))),
    (4, ((0, 1, 0, 1), (0, 3, 2, 3), (0, 1, 0, 3), (0, 3, 2, 3))),
    (4, ((3, 3, 1, 1), (3, 3, 1, 1), (3, 1, 1, 1), (1, 1, 1, 1))),
    (4, ((2, 0, 0, 3), (3, 2, 1, 2), (1, 2, 2, 2), (2, 2, 3, 2))),
    (4, ((0, 3, 1, 3), (3, 1, 2, 3), (0, 1, 2, 0), (0, 1, 2, 3))),
    (4, ((0, 1, 3, 1), (2, 1, 2, 3), (0, 1, 2, 1), (0, 1, 1, 3))),
    (4, ((2, 0, 3, 1), (3, 1, 1, 3), (3, 2, 2, 3), (0, 3, 1, 1))),
    (4, ((3, 2, 0, 1), (3, 0, 1, 2), (3, 0, 2, 1), (2, 0, 3, 1))),
    (4, ((0, 1, 3, 1), (2, 1, 2, 3), (0, 1, 2, 1), (0, 1, 2, 3))),
    (4, ((0, 3, 1, 3), (3, 3, 0, 3), (1, 3, 1, 3), (0, 3, 1, 3))),
    (4, ((2, 3, 0, 1), (1, 0, 3, 2), (1, 0, 3, 2), (2, 3, 0, 1))),
    (4, ((3, 3, 1, 1), (3, 3, 3, 3), (2, 3, 3, 1), (3, 3, 3, 3))),
    (4, ((0, 1, 2, 3), (1, 0, 0, 1), (1, 0, 3, 2), (3, 1, 1, 0))),
    (4, ((3, 1, 3, 1), (3, 3, 0, 3), (1, 3, 3, 3), (1, 3, 3, 3))),
    (4, ((1, 1, 1, 1), (2, 2, 2, 2), (0, 0, 3, 3), (1, 1, 1, 1))),
    (4, ((0, 0, 1, 3), (3, 1, 3, 1), (3, 1, 0, 2), (1, 3, 1, 3))),
    (4, ((2, 1, 0, 1), (2, 2, 1, 2), (2, 2, 2, 2), (0, 0, 3, 2))),
    (4, ((3, 3, 2, 3), (3, 2, 2, 3), (2, 2, 2, 3), (3, 3, 2, 3))),
    (4, ((0, 2, 3, 1), (3, 1, 0, 2), (1, 3, 2, 0), (2, 0, 1, 3))),
    (4, ((2, 0, 3, 1), (3, 1, 1, 3), (3, 2, 2, 3), (1, 3, 3, 1))),
    (4, ((0, 3, 0, 3), (2, 2, 1, 2), (1, 1, 2, 1), (3, 2, 3, 0))),
    (4, ((2, 2, 0, 3), (2, 2, 1, 0), (2, 2, 0, 3), (2, 3, 1, 0))),
    (4, ((3, 2, 2, 3), (3, 2, 2, 3), (1, 0, 1, 0), (1, 0, 1, 0))),
    (4, ((2, 2, 0, 3), (2, 2, 0, 1), (2, 3, 2, 2), (2, 3, 3, 2))),
    (4, ((3, 1, 1, 1), (3, 3, 0, 0), (2, 2, 2, 0), (2, 1, 1, 1))),
    (4, ((1, 0, 0, 3), (1, 3, 1, 0), (2, 0, 1, 0), (1, 0, 0, 3))),
    (4, ((2, 2, 0, 3), (2, 2, 3, 3), (0, 1, 3, 2), (3, 3, 2, 0))),
    (4, ((1, 0, 3, 3), (3, 2, 1, 3), (2, 3, 0, 3), (0, 1, 2, 3))),
    (4, ((3, 0, 1, 1), (1, 1, 1, 1), (1, 2, 0, 1), (0, 3, 1, 2))),
    (4, ((0, 3, 2, 3), (3, 0, 2, 2), (2, 1, 0, 1), (0, 2, 2, 3))),
    (4, ((3, 0, 0, 1), (3, 1, 1, 2), (1, 2, 2, 2), (2, 2, 3, 2))),
    (4, ((2, 0, 0, 3), (3, 0, 2, 0), (0, 3, 3, 2), (3, 1, 2, 0))),
    (4, ((2, 0, 3, 1), (3, 2, 1, 0), (0, 1, 2, 3), (1, 3, 0, 2))),
    (4, ((3, 3, 1, 3), (3, 3, 3, 3), (0, 0, 0, 0), (3, 3, 3, 3))),
    (4, ((1, 0, 0, 3), (1, 2, 1, 1), (3, 2, 3, 2), (1, 3, 3, 3))),
    (4, ((2, 2, 2, 3), (3, 2, 2, 3), (2, 2, 2, 3), (3, 2, 2, 3))),
    (4, ((2, 0, 0, 1), (3, 1, 1, 0), (0, 2, 2, 3), (1, 3, 3, 2))),
    (4, ((3, 2, 3, 1), (3, 1, 3, 2), (1, 2, 1, 3), (1, 3, 1, 1))),
    (4, ((1, 1, 2, 1), (3, 3, 3, 3), (1, 1, 1, 1), (0, 2, 2, 2))),
    (4, ((3, 0, 3, 3), (3, 3, 0, 3), (2, 0, 3, 3), (3, 0, 3, 3))),
    (4, ((0, 3, 1, 3), (3, 1, 2, 3), (3, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((0, 1, 2, 3), (2, 3, 3, 2), (3, 3, 1, 1), (1, 2, 1, 2))),
    (4, ((0, 0, 0, 1), (1, 1, 1, 0), (1, 2, 2, 2), (3, 0, 0, 3))),
    (4, ((2, 0, 1, 3), (3, 0, 2, 1), (2, 1, 3, 0), (0, 2, 3, 1))),
    (4, ((1, 3, 0, 1), (3, 2, 1, 0), (0, 1, 2, 3), (2, 0, 3, 2))),
    (4, ((1, 1, 3, 3), (3, 2, 2, 2), (0, 3, 0, 0), (0, 1, 2, 3))),
    (4, ((2, 2, 2, 3), (2, 3, 2, 3), (0, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((1, 1, 2, 1), (3, 3, 2, 3), (3, 0, 2, 1), (0, 0, 2, 0))),
    (4, ((3, 1, 1, 3), (3, 3, 2, 3), (2, 1, 3, 3), (0, 1, 2, 3))),
    (4, ((3, 0, 0, 1), (3, 0, 1, 1), (2, 2, 2, 2), (3, 0, 3, 1))),
    (4, ((1, 0, 0, 3), (1, 1, 1, 1), (2, 2, 2, 2), (2, 3, 3, 3))),
    (4, ((3, 3, 1, 1), (3, 3, 1, 2), (3, 3, 1, 2), (3, 0, 1, 1))),
    (4, ((2, 0, 1, 3), (3, 1, 0, 2), (0, 2, 3, 1), (1, 3, 2, 0))),
    (4, ((0, 0, 0, 1), (1, 1, 1, 0), (3, 3, 2, 2), (2, 2, 3, 3))),
    (4, ((0, 0, 3, 3), (2, 3, 2, 2), (1, 1, 2, 3), (0, 0, 2, 0))),
    (4, ((0, 2, 1, 3), (2, 0, 3, 1), (3, 1, 2, 0), (1, 3, 0, 2))),
    (4, ((1, 3, 0, 1), (3, 3, 1, 0), (3, 0, 2, 1), (1, 0, 3, 0))),
    (4, ((3, 0, 0, 1), (2, 0, 1, 1), (2, 3, 1, 2), (3, 3, 0, 2))),
    (4, ((2, 0, 1, 1), (3, 1, 3, 2), (1, 2, 0, 3), (0, 3, 2, 0))),
    (4, ((2, 3, 0, 1), (3, 2, 1, 0), (0, 1, 3, 2), (1, 0, 3, 2))),
    (4, ((2, 0, 0, 1), (2, 2, 1, 1), (2, 2, 2, 2), (0, 2, 3, 2))),
    (4, ((2, 1, 3, 1), (3, 1, 2, 3), (0, 1, 3, 1), (0, 1, 2, 1))),
    (4, ((2, 0, 3, 1), (2, 3, 0, 2), (0, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((3, 3, 1, 3), (3, 3, 3, 2), (0, 0, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 0, 1, 3), (3, 3, 3, 2), (1, 0, 3, 3), (3, 0, 3, 3))),
    (4, ((0, 2, 0, 1), (3, 2, 1, 1), (2, 2, 2, 2), (2, 2, 3, 3))),
    (4, ((1, 0, 0, 1), (1, 1, 1, 1), (2, 2, 1, 0), (3, 3, 2, 2))),
    (4, ((2, 0, 2, 3), (3, 0, 3, 2), (0, 1, 2, 3), (0, 1, 2, 2))),
    (4, ((3, 0, 3, 1), (3, 3, 1, 2), (2, 3, 3, 0), (3, 3, 3, 3))),
    (4, ((0, 2, 2, 3), (3, 0, 3, 0), (0, 1, 2, 3), (0, 2, 2, 3))),
    (4, ((3, 1, 3, 1), (2, 3, 2, 3), (2, 1, 3, 3), (2, 3, 3, 3))),
    (4, ((0, 0, 3, 3), (3, 0, 2, 3), (1, 0, 0, 1), (0, 1, 3, 0))),
    (4, ((3, 1, 3, 3), (3, 3, 3, 3), (3, 3, 1, 3), (3, 3, 3, 3))),
    (4, ((3, 1, 1, 3), (3, 3, 3, 3), (1, 0, 3, 3), (3, 3, 3, 3))),
    (4, ((1, 3, 0, 1), (2, 2, 1, 1), (2, 2, 2, 2), (1, 3, 3, 2))),
    (4, ((2, 2, 0, 1), (2, 0, 1, 2), (2, 2, 2, 2), (3, 3, 3, 0))),
    (4, ((3, 0, 3, 1), (3, 2, 3, 1), (2, 2, 3, 1), (3, 2, 3, 1))),
    (4, ((0, 2, 0, 0), (3, 3, 1, 1), (2, 2, 0, 2), (3, 3, 3, 3))),
    (4, ((0, 3, 1, 1), (0, 1, 3, 2), (0, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((3, 2, 3, 1), (3, 3, 0, 2), (1, 3, 3, 0), (2, 0, 1, 3))),
    (4, ((0, 0, 1, 0), (1, 1, 1, 0), (1, 2, 2, 1), (2, 3, 3, 3))),
    (4, ((0, 3, 1, 1), (3, 1, 2, 3), (0, 3, 2, 1), (0, 1, 2, 3))),
    (4, ((3, 3, 3, 1), (3, 2, 0, 0), (3, 0, 1, 0), (0, 1, 2, 3))),
    (4, ((0, 0, 3, 0), (3, 1, 0, 1), (2, 2, 2, 2), (3, 0, 0, 3))),
    (4, ((2, 3, 3, 3), (3, 3, 2, 3), (2, 3, 1, 3), (0, 1, 2, 3))),
    (4, ((3, 2, 0, 1), (1, 2, 1, 1), (2, 2, 2, 2), (2, 0, 3, 3))),
    (4, ((3, 2, 3, 3), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((3, 0, 0, 3), (1, 1, 1, 1), (1, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((0, 2, 0, 1), (3, 1, 0, 1), (3, 1, 3, 1), (0, 2, 0, 2))),
    (4, ((1, 1, 3, 3), (3, 2, 0, 3), (0, 3, 3, 3), (0, 1, 2, 3))),
    (4, ((0, 0, 3, 0), (1, 1, 1, 1), (2, 3, 2, 2), (3, 2, 0, 3))),
    (4, ((1, 1, 1, 3), (3, 3, 2, 2), (0, 1, 0, 0), (0, 2, 0, 2))),
    (4, ((0, 0, 2, 3), (2, 2, 2, 3), (0, 1, 2, 2), (0, 1, 1, 0))),
    (4, ((2, 0, 0, 1), (2, 2, 1, 3), (2, 2, 2, 2), (3, 2, 3, 2))),
    (4, ((3, 2, 3, 1), (3, 2, 1, 3), (1, 1, 3, 2), (2, 3, 2, 1))),
    (4, ((2, 2, 2, 3), (3, 3, 2, 3), (2, 2, 2, 3), (3, 3, 2, 3))),
    (4, ((1, 1, 3, 3), (2, 2, 2, 3), (0, 0, 0, 3), (0, 1, 2, 3))),
    (4, ((3, 1, 3, 3), (2, 3, 2, 3), (2, 1, 3, 3), (0, 1, 2, 3))),
    (4, ((0, 1, 3, 3), (3, 1, 0, 2), (0, 1, 2, 0), (0, 1, 2, 3))),
    (4, ((3, 1, 3, 3), (3, 3, 3, 3), (2, 0, 3, 3), (0, 1, 2, 3))),
    (4, ((1, 2, 0, 3), (3, 2, 1, 3), (2, 1, 3, 2), (1, 3, 2, 1))),
    (4, ((1, 0, 2, 3), (1, 0, 3, 2), (0, 1, 2, 3), (2, 1, 0, 3))),
    (4, ((0, 3, 3, 3), (3, 1, 2, 2), (3, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((3, 1, 3, 1), (2, 3, 2, 3), (2, 1, 2, 1), (2, 3, 2, 3))),
    (4, ((0, 1, 3, 1), (3, 2, 3, 1), (2, 0, 1, 0), (2, 0, 2, 3))),
    (4, ((0, 0, 3, 3), (3, 3, 2, 2), (1, 1, 2, 3), (0, 0, 2, 3))),
    (4, ((3, 2, 0, 1), (3, 2, 0, 1), (2, 3, 1, 0), (2, 3, 1, 0))),
    (4, ((3, 1, 1, 3), (3, 3, 1, 3), (3, 0, 0, 3), (0, 1, 2, 3))),
    (4, ((1, 0, 0, 1), (3, 3, 3, 2), (0, 3, 3, 0), (2, 0, 1, 1))),
    (4, ((0, 3, 0, 3), (2, 3, 2, 3), (2, 1, 2, 1), (0, 1, 0, 1))),
    (4, ((0, 3, 2, 3), (3, 3, 3, 3), (0, 0, 0, 3), (0, 1, 2, 3))),
    (4, ((3, 1, 3, 3), (3, 3, 2, 3), (0, 3, 3, 3), (2, 0, 1, 3))),
    (4, ((0, 1, 2, 3), (2, 0, 1, 3), (1, 2, 0, 3), (1, 2, 0, 3))),
    (4, ((1, 0, 0, 1), (1, 1, 1, 1), (2, 2, 2, 2), (1, 3, 3, 2))),
    (4, ((2, 3, 2, 3), (3, 2, 2, 3), (0, 1, 2, 3), (0, 1, 2, 2))),
    (4, ((1, 0, 0, 1), (3, 1, 1, 3), (3, 2, 2, 0), (1, 3, 3, 2))),
    (4, ((0, 2, 3, 3), (2, 1, 2, 3), (0, 3, 2, 3), (0, 1, 2, 3))),
    (4, ((0, 3, 1, 0), (3, 1, 1, 1), (3, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((0, 0, 0, 1), (1, 1, 0, 1), (2, 0, 2, 0), (3, 3, 0, 3))),
    (4, ((1, 3, 1, 3), (3, 3, 1, 3), (3, 3, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 1, 3, 3), (3, 3, 3, 3), (1, 1, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 1, 3, 3), (3, 1, 1, 3), (1, 1, 1, 3), (3, 1, 1, 3))),
    (4, ((2, 1, 2, 3), (2, 1, 2, 3), (2, 1, 2, 3), (1, 1, 2, 3))),
    (4, ((2, 1, 2, 3), (3, 3, 3, 2), (0, 0, 0, 0), (1, 2, 1, 1))),
    (4, ((3, 2, 3, 1), (2, 2, 3, 0), (2, 0, 1, 1), (2, 0, 1, 0))),
    (4, ((1, 1, 2, 1), (3, 1, 2, 0), (3, 1, 2, 0), (1, 1, 2, 2))),
    (4, ((2, 2, 3, 3), (3, 3, 2, 2), (1, 1, 0, 0), (0, 0, 1, 1))),
    (4, ((0, 3, 3, 3), (1, 1, 2, 2), (1, 1, 2, 2), (0, 3, 3, 3))),
    (4, ((3, 3, 1, 3), (3, 3, 3, 3), (2, 3, 3, 3), (3, 0, 3, 3))),
    (4, ((3, 0, 3, 1), (2, 3, 1, 2), (1, 2, 3, 1), (3, 3, 3, 3))),
    (4, ((2, 2, 0, 3), (2, 2, 0, 3), (0, 1, 2, 3), (0, 0, 3, 2))),
    (4, ((1, 0, 3, 1), (3, 1, 0, 3), (1, 2, 1, 0), (2, 3, 2, 1))),
    (4, ((3, 0, 1, 1), (3, 0, 1, 1), (3, 1, 0, 2), (3, 0, 0, 1))),
    (4, ((2, 2, 1, 1), (3, 3, 3, 3), (3, 3, 0, 0), (1, 1, 1, 1))),
    (4, ((3, 1, 0, 1), (3, 1, 0, 1), (3, 1, 0, 1), (3, 3, 0, 3))),
    (4, ((3, 1, 3, 3), (2, 2, 2, 2), (1, 1, 1, 1), (3, 3, 3, 3))),
    (4, ((1, 3, 1, 3), (3, 3, 3, 3), (0, 3, 1, 3), (3, 3, 3, 3))),
    (4, ((3, 0, 1, 1), (1, 2, 0, 0), (2, 2, 2, 2), (2, 2, 3, 3))),
    (4, ((0, 1, 2, 3), (2, 3, 1, 0), (1, 2, 3, 0), (1, 3, 0, 2))),
    (4, ((1, 2, 2, 1), (3, 1, 2, 3), (3, 1, 2, 3), (0, 1, 1, 3))),
    (4, ((3, 1, 0, 1), (2, 2, 1, 2), (2, 2, 2, 2), (2, 2, 3, 2))),
    (4, ((0, 3, 0, 3), (3, 1, 3, 3), (2, 3, 2, 3), (2, 1, 0, 3))),
    (4, ((2, 3, 3, 1), (3, 0, 3, 2), (3, 3, 1, 0), (3, 3, 3, 3))),
    (4, ((2, 1, 0, 1), (2, 2, 1, 0), (2, 2, 2, 2), (2, 3, 3, 2))),
    (4, ((3, 1, 1, 1), (3, 1, 1, 1), (2, 3, 3, 3), (2, 3, 3, 3))),
    (4, ((3, 2, 3, 3), (3, 0, 0, 3), (1, 3, 3, 3), (0, 1, 2, 3))),
    (4, ((3, 1, 3, 3), (2, 2, 2, 1), (0, 1, 1, 1), (0, 0, 2, 0))),
    (4, ((0, 2, 1, 3), (0, 1, 2, 3), (3, 1, 2, 0), (0, 1, 2, 3))),
    (4, ((1, 1, 1, 1), (2, 3, 2, 3), (3, 1, 3, 3), (0, 1, 2, 3))),
    (4, ((2, 2, 1, 1), (3, 3, 3, 2), (1, 0, 0, 3), (0, 1, 2, 0))),
    (4, ((3, 1, 1, 1), (1, 1, 1, 1), (1, 3, 1, 1), (3, 3, 3, 3))),
    (4, ((2, 1, 0, 3), (2, 1, 3, 0), (2, 1, 0, 3), (2, 0, 1, 3))),
    (4, ((2, 2, 1, 3), (3, 3, 3, 3), (1, 1, 0, 3), (0, 1, 2, 0))),
    (4, ((0, 1, 3, 3), (2, 3, 3, 0), (3, 1, 0, 3), (0, 3, 2, 0))),
    (4, ((0, 1, 1, 1), (2, 3, 3, 3), (3, 0, 0, 0), (1, 2, 2, 2))),
    (4, ((3, 3, 2, 1), (3, 3, 2, 0), (0, 1, 3, 2), (2, 2, 0, 3))),
    (4, ((1, 2, 1, 3), (3, 2, 1, 3), (1, 2, 1, 3), (1, 2, 1, 3))),
    (4, ((3, 3, 3, 1), (3, 3, 3, 3), (0, 0, 0, 0), (2, 0, 2, 0))),
    (4, ((3, 2, 3, 3), (3, 3, 3, 3), (2, 3, 3, 3), (1, 2, 3, 3))),
    (4, ((3, 0, 3, 1), (3, 2, 3, 1), (0, 2, 3, 1), (3, 2, 3, 1))),
    (4, ((3, 2, 0, 1), (2, 3, 1, 0), (0, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((3, 3, 1, 1), (3, 2, 3, 2), (0, 0, 1, 0), (2, 2, 0, 0))),
    (4, ((3, 1, 3, 3), (2, 3, 0, 3), (0, 3, 3, 3), (0, 1, 2, 3))),
    (4, ((3, 3, 1, 3), (3, 3, 3, 3), (2, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((2, 2, 0, 1), (3, 2, 0, 2), (0, 1, 2, 3), (2, 0, 1, 2))),
    (4, ((3, 2, 0, 1), (2, 3, 0, 1), (2, 3, 1, 0), (2, 3, 0, 1))),
    (4, ((3, 2, 3, 1), (3, 1, 2, 1), (1, 2, 2, 3), (2, 1, 3, 3))),
    (4, ((2, 0, 3, 1), (2, 1, 1, 2), (2, 2, 1, 2), (2, 3, 3, 1))),
    (4, ((1, 1, 2, 1), (3, 3, 3, 3), (3, 2, 3, 3), (0, 0, 0, 0))),
    (4, ((3, 0, 3, 1), (1, 3, 1, 2), (2, 2, 0, 1), (3, 3, 0, 3))),
    (4, ((0, 0, 2, 3), (2, 1, 0, 2), (2, 1, 0, 2), (0, 0, 2, 1))),
    (4, ((0, 0, 0, 1), (1, 1, 1, 2), (2, 2, 0, 3), (3, 3, 1, 0))),
    (4, ((3, 2, 2, 3), (3, 3, 3, 3), (2, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((0, 1, 2, 3), (0, 1, 2, 3), (0, 1, 2, 3), (1, 2, 0, 3))),
    (4, ((0, 0, 2, 3), (2, 2, 2, 0), (0, 1, 2, 3), (1, 2, 2, 1))),
    (4, ((3, 1, 0, 1), (2, 1, 0, 1), (2, 1, 1, 1), (2, 3, 0, 3))),
    (4, ((3, 2, 0, 1), (2, 0, 3, 1), (2, 3, 1, 0), (1, 3, 0, 2))),
    (4, ((0, 0, 0, 1), (1, 2, 0, 1), (2, 2, 3, 0), (3, 0, 3, 1))),
    (4, ((1, 2, 2, 1), (3, 3, 0, 0), (3, 3, 2, 0), (3, 3, 2, 1))),
    (4, ((3, 2, 3, 3), (3, 3, 3, 3), (3, 3, 1, 3), (3, 3, 3, 3))),
    (4, ((3, 2, 3, 3), (1, 1, 1, 1), (2, 0, 2, 2), (0, 3, 0, 0))),
    (4, ((3, 2, 0, 1), (3, 2, 0, 1), (1, 0, 2, 3), (1, 0, 3, 2))),
    (4, ((0, 3, 2, 3), (3, 2, 1, 0), (2, 1, 0, 1), (3, 2, 1, 0))),
    (4, ((0, 2, 3, 1), (2, 0, 1, 3), (3, 1, 0, 2), (1, 3, 2, 0))),
    (4, ((3, 0, 2, 3), (3, 3, 0, 3), (0, 1, 0, 3), (0, 1, 2, 2))),
    (4, ((0, 3, 0, 1), (2, 2, 1, 1), (2, 2, 2, 2), (2, 3, 3, 2))),
    (4, ((3, 1, 3, 1), (3, 1, 1, 1), (3, 1, 0, 1), (3, 1, 1, 1))),
    (4, ((2, 0, 0, 3), (2, 2, 1, 3), (0, 3, 3, 2), (3, 1, 2, 0))),
    (4, ((3, 2, 2, 3), (3, 3, 3, 3), (1, 1, 0, 0), (0, 0, 0, 0))),
    (4, ((2, 1, 1, 1), (3, 0, 0, 3), (0, 0, 3, 0), (2, 2, 2, 1))),
    (4, ((0, 1, 2, 3), (1, 0, 3, 2), (3, 2, 1, 0), (2, 3, 0, 1))),
    (4, ((0, 1, 2, 3), (0, 1, 2, 3), (2, 3, 0, 1), (3, 2, 1, 0))),
    (4, ((2, 1, 3, 3), (2, 3, 0, 3), (0, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((3, 2, 3, 3), (3, 3, 3, 3), (2, 2, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 2, 0, 1), (3, 2, 1, 0), (3, 2, 1, 0), (2, 3, 1, 0))),
    (4, ((3, 1, 3, 3), (3, 3, 1, 3), (0, 0, 0, 0), (3, 3, 0, 3))),
    (4, ((2, 2, 1, 1), (3, 3, 0, 0), (3, 3, 1, 1), (2, 2, 0, 0))),
    (4, ((3, 2, 1, 1), (3, 0, 3, 2), (2, 2, 2, 2), (2, 0, 0, 1))),
    (4, ((1, 0, 2, 3), (1, 0, 2, 3), (0, 3, 2, 1), (1, 0, 2, 3))),
    (4, ((3, 1, 3, 1), (3, 3, 3, 3), (1, 3, 3, 0), (3, 3, 3, 3))),
    (4, ((0, 3, 1, 1), (3, 1, 3, 2), (1, 0, 2, 0), (2, 2, 0, 3))),
    (4, ((0, 1, 3, 3), (3, 1, 3, 2), (1, 3, 2, 3), (0, 1, 2, 3))),
    (4, ((2, 1, 3, 1), (2, 2, 3, 3), (2, 2, 3, 3), (0, 1, 2, 3))),
    (4, ((2, 2, 0, 1), (3, 3, 0, 0), (0, 0, 0, 0), (1, 1, 1, 1))),
    (4, ((0, 3, 0, 3), (2, 2, 2, 2), (1, 1, 1, 1), (3, 0, 3, 0))),
    (4, ((2, 2, 2, 3), (3, 2, 0, 3), (2, 0, 2, 0), (3, 3, 0, 3))),
    (4, ((3, 1, 3, 3), (3, 3, 0, 3), (3, 0, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 0, 3, 3), (3, 3, 0, 3), (3, 1, 3, 3), (3, 0, 3, 3))),
    (4, ((3, 3, 1, 3), (3, 3, 3, 3), (2, 1, 3, 3), (3, 3, 3, 3))),
    (4, ((0, 1, 2, 3), (2, 1, 0, 3), (3, 1, 2, 0), (1, 0, 2, 3))),
    (4, ((0, 0, 0, 1), (1, 1, 0, 0), (2, 3, 2, 2), (3, 0, 0, 3))),
    (4, ((0, 3, 0, 3), (2, 2, 0, 0), (0, 2, 0, 3), (0, 2, 2, 0))),
    (4, ((3, 2, 0, 1), (2, 3, 1, 0), (2, 3, 1, 0), (3, 2, 0, 1))),
    (4, ((2, 1, 1, 3), (3, 3, 3, 1), (0, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((0, 1, 1, 3), (3, 3, 1, 3), (3, 0, 0, 3), (0, 1, 2, 3))),
    (4, ((3, 0, 1, 3), (3, 3, 1, 3), (0, 3, 3, 0), (0, 1, 2, 3))),
    (4, ((0, 2, 2, 3), (2, 1, 2, 3), (0, 1, 2, 0), (0, 1, 1, 3))),
    (4, ((3, 2, 3, 3), (3, 3, 0, 3), (3, 3, 3, 3), (3, 3, 3, 3))),
    (4, ((0, 3, 2, 1), (0, 3, 2, 1), (2, 1, 0, 3), (2, 1, 0, 3))),
    (4, ((0, 0, 0, 1), (1, 1, 0, 1), (2, 0, 2, 2), (2, 3, 3, 3))),
    (4, ((2, 2, 0, 1), (2, 1, 1, 1), (2, 2, 2, 2), (2, 3, 3, 1))),
    (4, ((3, 1, 3, 3), (3, 3, 0, 3), (0, 3, 1, 3), (0, 1, 2, 3))),
    (4, ((2, 2, 3, 3), (3, 3, 2, 2), (0, 0, 1, 1), (1, 1, 0, 0))),
    (4, ((2, 3, 1, 1), (3, 0, 0, 0), (0, 0, 0, 0), (1, 3, 0, 0))),
    (4, ((3, 1, 0, 3), (3, 3, 2, 3), (3, 0, 3, 1), (0, 1, 2, 3))),
    (4, ((1, 0, 0, 1), (3, 1, 2, 3), (0, 2, 1, 2), (2, 3, 2, 1))),
    (4, ((0, 1, 2, 3), (2, 3, 0, 1), (3, 2, 1, 0), (1, 0, 3, 2))),
    (4, ((1, 0, 0, 2), (3, 1, 1, 1), (1, 2, 2, 2), (3, 3, 3, 2))),
    (4, ((3, 2, 1, 3), (3, 3, 2, 0), (3, 3, 3, 3), (3, 3, 3, 3))),
    (4, ((0, 0, 3, 3), (2, 2, 1, 1), (1, 1, 2, 2), (3, 3, 0, 0))),
    (4, ((0, 1, 1, 3), (3, 0, 3, 0), (3, 0, 3, 0), (3, 3, 0, 0))),
    (4, ((0, 3, 1, 3), (3, 0, 3, 1), (2, 2, 3, 1), (0, 3, 0, 3))),
    (4, ((3, 1, 3, 1), (3, 1, 3, 1), (2, 0, 2, 0), (2, 2, 2, 0))),
    (4, ((3, 2, 0, 3), (3, 2, 1, 1), (2, 1, 2, 2), (1, 2, 3, 1))),
    (4, ((1, 3, 0, 3), (3, 2, 1, 2), (2, 2, 2, 2), (2, 1, 3, 1))),
    (4, ((2, 1, 0, 1), (2, 2, 1, 1), (2, 2, 2, 2), (2, 2, 3, 2))),
    (4, ((2, 3, 0, 0), (3, 2, 1, 1), (2, 2, 2, 2), (3, 3, 3, 2))),
    (4, ((1, 0, 2, 1), (3, 2, 1, 2), (2, 1, 0, 3), (3, 0, 1, 0))),
    (4, ((0, 0, 0, 0), (2, 1, 1, 1), (3, 2, 2, 2), (1, 3, 3, 3))),
    (4, ((3, 1, 1, 3), (3, 2, 3, 3), (0, 3, 3, 3), (0, 1, 2, 3))),
    (4, ((3, 3, 1, 1), (2, 3, 0, 0), (2, 2, 3, 2), (3, 3, 3, 3))),
    (4, ((2, 3, 1, 3), (3, 0, 2, 2), (1, 1, 3, 0), (0, 2, 0, 1))),
    (4, ((2, 2, 1, 1), (3, 3, 0, 0), (2, 2, 0, 0), (3, 3, 1, 1))),
    (4, ((3, 2, 2, 3), (3, 2, 2, 3), (2, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((3, 1, 1, 3), (2, 3, 3, 3), (0, 1, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 1, 3, 1), (3, 0, 0, 3), (2, 2, 2, 2), (0, 0, 0, 1))),
    (4, ((3, 0, 3, 3), (3, 3, 3, 3), (2, 2, 3, 3), (3, 3, 3, 3))),
    (4, ((0, 1, 2, 3), (1, 0, 0, 0), (2, 2, 0, 0), (3, 2, 0, 0))),
    (4, ((0, 0, 3, 1), (3, 2, 3, 1), (1, 2, 3, 1), (2, 2, 3, 1))),
    (4, ((3, 1, 0, 1), (2, 2, 1, 2), (2, 2, 2, 2), (2, 1, 3, 1))),
    (4, ((1, 3, 0, 1), (2, 1, 3, 1), (1, 1, 1, 2), (2, 3, 3, 3))),
    (4, ((2, 0, 1, 3), (3, 1, 0, 2), (1, 3, 2, 0), (0, 2, 3, 1))),
    (4, ((3, 1, 3, 1), (3, 1, 3, 1), (2, 0, 2, 0), (2, 0, 2, 0))),
    (4, ((1, 3, 0, 1), (3, 1, 2, 3), (0, 2, 1, 0), (1, 3, 0, 1))),
    (4, ((1, 2, 3, 1), (3, 3, 3, 0), (3, 0, 0, 0), (2, 0, 1, 2))),
    (4, ((2, 0, 1, 1), (3, 1, 1, 1), (3, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((2, 2, 2, 3), (3, 3, 3, 2), (0, 1, 0, 0), (1, 0, 1, 1))),
    (4, ((3, 0, 3, 1), (3, 0, 3, 1), (3, 2, 3, 1), (3, 2, 3, 1))),
    (4, ((0, 2, 0, 0), (1, 1, 1, 0), (2, 3, 2, 2), (2, 3, 3, 3))),
    (4, ((0, 2, 0, 1), (2, 3, 1, 1), (2, 1, 2, 2), (1, 3, 0, 2))),
    (4, ((3, 2, 0, 1), (3, 2, 1, 0), (3, 2, 1, 0), (3, 1, 2, 0))),
    (4, ((2, 3, 3, 3), (3, 2, 2, 2), (1, 1, 1, 0), (0, 0, 0, 1))),
    (4, ((0, 3, 2, 1), (3, 0, 1, 2), (2, 1, 0, 3), (1, 2, 3, 0))),
    (4, ((0, 1, 0, 1), (2, 1, 2, 1), (2, 3, 2, 3), (0, 3, 0, 3))),
    (4, ((2, 3, 1, 1), (2, 0, 3, 2), (1, 0, 3, 1), (2, 0, 0, 1))),
    (4, ((0, 1, 1, 3), (3, 1, 2, 1), (2, 0, 2, 0), (2, 0, 3, 1))),
    (4, ((3, 2, 0, 1), (3, 1, 1, 2), (1, 2, 0, 0), (1, 3, 2, 2))),
    (4, ((2, 1, 0, 1), (3, 1, 0, 2), (1, 0, 3, 2), (0, 3, 1, 0))),
    (4, ((0, 2, 3, 3), (3, 1, 2, 0), (0, 2, 1, 3), (3, 1, 2, 0))),
    (4, ((3, 0, 1, 3), (3, 3, 0, 3), (2, 2, 3, 3), (3, 3, 3, 3))),
    (4, ((2, 0, 1, 1), (3, 0, 3, 1), (2, 0, 3, 0), (2, 2, 3, 1))),
    (4, ((3, 2, 3, 3), (3, 3, 3, 3), (3, 3, 0, 3), (3, 3, 3, 3))),
    (4, ((0, 3, 1, 3), (1, 1, 0, 1), (2, 3, 2, 2), (0, 0, 3, 3))),
    (4, ((0, 0, 2, 3), (2, 3, 2, 3), (0, 1, 2, 3), (0, 1, 2, 3))),
    (4, ((0, 0, 3, 3), (1, 1, 1, 3), (0, 2, 2, 2), (1, 1, 3, 3))),
    (4, ((3, 3, 1, 3), (3, 3, 3, 3), (3, 0, 3, 0), (3, 3, 3, 3))),
    (4, ((1, 1, 1, 1), (2, 2, 3, 2), (3, 3, 2, 3), (3, 3, 2, 3))),
    (4, ((3, 3, 2, 3), (3, 3, 3, 3), (1, 1, 1, 0), (0, 1, 0, 1))),
    (4, ((3, 0, 3, 3), (3, 3, 3, 0), (2, 0, 3, 3), (3, 0, 3, 3))),
    (4, ((3, 2, 0, 1), (3, 3, 0, 1), (3, 2, 1, 1), (3, 3, 1, 1))),
    (4, ((1, 1, 2, 3), (1, 1, 2, 3), (0, 0, 2, 3), (2, 1, 2, 3))),
    (4, ((2, 2, 2, 3), (3, 3, 3, 2), (3, 3, 2, 0), (0, 1, 2, 2))),
    (4, ((2, 1, 0, 1), (2, 3, 1, 1), (2, 3, 0, 2), (0, 3, 0, 1))),
    (4, ((0, 0, 1, 0), (3, 1, 3, 1), (2, 2, 2, 2), (1, 3, 0, 3))),
    (4, ((0, 2, 0, 1), (1, 2, 1, 1), (2, 1, 2, 2), (3, 2, 3, 0))),
    (4, ((3, 0, 3, 3), (1, 2, 2, 1), (2, 1, 1, 2), (0, 3, 0, 0))),
    (4, ((3, 1, 0, 3), (3, 1, 1, 1), (2, 2, 2, 2), (2, 3, 3, 3))),
    (4, ((0, 2, 1, 3), (3, 0, 0, 1), (3, 0, 2, 2), (2, 3, 3, 0))),
    (4, ((2, 1, 0, 3), (3, 0, 1, 2), (0, 3, 2, 1), (1, 2, 3, 0))),
    (4, ((3, 3, 1, 1), (3, 3, 3, 2), (3, 3, 2, 0), (2, 0, 1, 1))),
    (4, ((3, 3, 1, 3), (3, 3, 0, 3), (0, 1, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 2, 2, 3), (3, 2, 0, 3), (3, 0, 3, 3), (0, 1, 2, 3))),
    (4, ((1, 0, 0, 3), (0, 3, 3, 1), (0, 3, 3, 2), (3, 1, 0, 0))),
    (4, ((3, 1, 0, 1), (3, 2, 1, 1), (2, 2, 2, 2), (2, 2, 3, 3))),
    (4, ((3, 2, 0, 1), (3, 3, 0, 2), (1, 3, 3, 2), (0, 1, 2, 3))),
    (4, ((3, 1, 3, 1), (3, 1, 3, 1), (2, 0, 2, 0), (2, 0, 2, 1))),
    (4, ((2, 2, 0, 3), (2, 3, 1, 0), (2, 2, 1, 2), (2, 0, 3, 1))),
    (4, ((0, 3, 0, 3), (3, 0, 0, 3), (3, 2, 1, 3), (0, 1, 2, 0))),
    (4, ((3, 3, 1, 3), (3, 3, 1, 3), (3, 0, 1, 3), (3, 3, 1, 3))),
    (4, ((1, 2, 3, 3), (2, 2, 2, 2), (3, 3, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 0, 1, 3), (3, 3, 2, 3), (0, 3, 3, 3), (0, 1, 2, 3))),
    (4, ((1, 1, 1, 3), (3, 1, 2, 0), (3, 1, 2, 0), (0, 1, 1, 2))),
    (4, ((3, 1, 3, 1), (3, 1, 3, 1), (2, 0, 2, 0), (2, 2, 2, 2))),
    (4, ((3, 1, 0, 1), (2, 2, 1, 2), (2, 2, 2, 2), (2, 3, 3, 2))),
    (4, ((3, 2, 2, 3), (3, 3, 2, 0), (2, 2, 2, 0), (3, 0, 0, 3))),
    (4, ((1, 3, 1, 3), (3, 3, 3, 3), (3, 3, 1, 3), (3, 3, 3, 3))),
    (4, ((1, 1, 2, 1), (3, 3, 3, 3), (3, 3, 1, 3), (0, 0, 0, 0))),
    (4, ((2, 0, 2, 3), (3, 0, 2, 3), (0, 1, 2, 3), (1, 1, 2, 2))),
    (4, ((3, 3, 1, 3), (3, 3, 3, 3), (3, 3, 0, 3), (3, 3, 0, 3))),
    (4, ((0, 0, 0, 0), (2, 1, 1, 1), (1, 3, 2, 2), (1, 3, 3, 3))),
    (4, ((0, 3, 1, 3), (3, 1, 2, 3), (3, 1, 2, 3), (0, 1, 1, 3))),
    (4, ((2, 1, 1, 1), (3, 1, 0, 2), (1, 1, 3, 1), (1, 1, 1, 0))),
    (4, ((3, 3, 2, 3), (3, 3, 2, 3), (1, 3, 2, 3), (3, 3, 2, 3))),
    (4, ((1, 0, 0, 3), (1, 1, 1, 1), (2, 2, 1, 1), (2, 3, 0, 1))),
    (4, ((3, 0, 3, 1), (3, 1, 0, 3), (2, 0, 1, 0), (0, 1, 2, 3))),
    (4, ((3, 1, 3, 1), (3, 3, 1, 3), (0, 0, 3, 0), (3, 3, 1, 3))),
    (4, ((0, 0, 0, 1), (1, 1, 0, 1), (2, 2, 2, 0), (2, 3, 1, 3))),
    (4, ((1, 2, 2, 1), (3, 3, 2, 2), (3, 0, 2, 1), (2, 0, 2, 0))),
    (4, ((3, 3, 2, 3), (3, 2, 2, 3), (2, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((1, 2, 2, 1), (3, 3, 3, 3), (3, 3, 3, 3), (3, 3, 3, 3))),
    (4, ((3, 2, 3, 3), (2, 2, 2, 2), (2, 2, 2, 2), (3, 3, 3, 3))),
    (4, ((2, 2, 0, 1), (3, 0, 1, 0), (2, 2, 2, 2), (1, 2, 3, 2))),
    (4, ((0, 0, 1, 0), (1, 1, 1, 1), (2, 2, 2, 0), (1, 3, 3, 3))),
    (4, ((2, 2, 0, 1), (3, 3, 3, 2), (2, 2, 2, 3), (2, 1, 3, 2))),
    (4, ((2, 2, 1, 1), (3, 0, 3, 0), (3, 0, 3, 0), (2, 2, 1, 1))),
    (4, ((3, 1, 0, 1), (3, 2, 1, 0), (2, 2, 2, 2), (2, 2, 3, 2))),
    (4, ((3, 2, 0, 1), (2, 1, 1, 2), (2, 2, 2, 2), (2, 0, 3, 1))),
    (4, ((1, 2, 0, 3), (3, 0, 2, 1), (2, 1, 3, 0), (0, 3, 1, 2))),
    (4, ((0, 3, 0, 3), (2, 2, 1, 1), (2, 2, 1, 1), (0, 3, 0, 3))),
    (4, ((1, 2, 1, 1), (3, 3, 3, 2), (0, 1, 2, 3), (2, 0, 0, 0))),
    (4, ((0, 2, 1, 3), (2, 3, 1, 0), (3, 0, 1, 2), (1, 3, 0, 2))),
    (4, ((0, 2, 1, 3), (1, 0, 2, 3), (2, 3, 0, 1), (3, 1, 2, 0))),
    (4, ((1, 0, 3, 1), (1, 1, 1, 1), (1, 2, 1, 2), (1, 3, 3, 1))),
    (4, ((2, 3, 1, 1), (3, 3, 0, 1), (3, 1, 0, 1), (2, 3, 1, 1))),
    (4, ((1, 0, 0, 1), (1, 1, 1, 1), (2, 2, 3, 1), (0, 3, 3, 0))),
    (4, ((0, 2, 1, 3), (0, 1, 2, 3), (0, 1, 2, 3), (1, 0, 2, 3))),
    (4, ((3, 3, 1, 3), (3, 3, 1, 3), (3, 3, 0, 3), (0, 1, 2, 3))),
    (4, ((3, 2, 3, 1), (3, 1, 1, 3), (1, 1, 2, 2), (2, 3, 2, 3))),
    (4, ((2, 2, 0, 1), (3, 3, 0, 1), (3, 2, 1, 1), (3, 2, 0, 0))),
    (4, ((3, 1, 3, 3), (3, 2, 2, 2), (1, 3, 3, 3), (3, 3, 2, 2))),
    (4, ((3, 0, 0, 1), (1, 2, 0, 1), (3, 2, 0, 2), (3, 2, 3, 1))),
    (4, ((0, 1, 3, 1), (3, 1, 3, 1), (2, 0, 2, 0), (2, 0, 2, 3))),
    (4, ((3, 0, 3, 1), (3, 0, 3, 1), (3, 2, 0, 1), (3, 0, 3, 1))),
    (4, ((3, 3, 1, 1), (3, 2, 1, 0), (3, 1, 1, 1), (3, 2, 1, 0))),
    (4, ((0, 1, 2, 1), (3, 2, 3, 2), (0, 1, 2, 3), (2, 1, 0, 0))),
    (4, ((3, 2, 0, 1), (3, 2, 0, 1), (3, 2, 0, 1), (3, 2, 0, 1))),
    (4, ((1, 0, 0, 1), (3, 1, 2, 3), (2, 3, 1, 0), (1, 3, 1, 1))),
    (4, ((3, 0, 0, 1), (2, 3, 1, 0), (1, 2, 3, 2), (0, 1, 2, 3))),
    (4, ((3, 0, 1, 3), (1, 2, 2, 0), (0, 3, 0, 2), (2, 1, 3, 1))),
    (4, ((0, 3, 1, 3), (3, 1, 2, 3), (0, 3, 2, 3), (0, 1, 2, 3))),
    (4, ((1, 1, 3, 1), (2, 1, 3, 2), (0, 1, 1, 3), (0, 1, 2, 1))),
    (4, ((0, 1, 3, 3), (3, 1, 2, 2), (0, 1, 2, 3), (1, 2, 2, 3))),
    (4, ((3, 3, 1, 3), (3, 3, 1, 3), (1, 1, 0, 0), (3, 3, 1, 3))),
    (4, ((0, 2, 1, 3), (0, 1, 3, 2), (3, 1, 2, 0), (1, 0, 2, 3))),
    (4, ((0, 3, 3, 3), (2, 3, 2, 3), (1, 1, 3, 3), (0, 1, 2, 3))),
    (5, ((0, 2, 0, 4, 0), (3, 1, 1, 1, 1), (3, 2, 2, 2, 3), (3, 2, 3, 3, 3), (4, 4, 0, 4, 4))),
    (6, ((0, 2, 0, 4, 5, 0), (1, 1, 0, 0, 1, 0), (3, 2, 2, 2, 2, 4), (3, 3, 1, 3, 3, 4), (4, 4, 0, 0, 4, 1), (2, 2, 5, 5, 5, 5))),
    (5, ((0, 0, 3, 0, 1), (2, 1, 1, 1, 1), (3, 4, 2, 2, 2), (3, 4, 3, 3, 3), (3, 4, 3, 4, 4))),
    (5, ((0, 2, 0, 0, 2), (1, 1, 4, 1, 1), (3, 3, 2, 2, 2), (4, 4, 4, 3, 3), (3, 4, 3, 4, 4))),
    (6, ((0, 3, 3, 0, 5, 0), (5, 1, 4, 1, 1, 1), (5, 4, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3), (5, 4, 4, 4, 4, 4), (5, 5, 5, 5, 5, 5))),
    (5, ((4, 3, 0, 1, 0), (2, 4, 0, 1, 1), (2, 3, 4, 1, 2), (2, 3, 0, 4, 3), (4, 4, 4, 4, 4))),
    (5, ((1, 2, 3, 0, 4), (4, 0, 2, 1, 3), (3, 1, 4, 2, 0), (2, 4, 0, 3, 1), (0, 3, 1, 4, 2))),
    (8, ((5, 3, 4, 6, 0, 7, 2, 1), (2, 5, 6, 7, 3, 4, 1, 0), (6, 0, 5, 1, 7, 2, 4, 3), (3, 2, 0, 5, 1, 6, 7, 4), (7, 6, 3, 4, 5, 1, 0, 2), (0, 1, 2, 3, 4, 5, 6, 7), (1, 4, 7, 0, 2, 3, 5, 6), (4, 7, 1, 2, 6, 0, 3, 5))),
    (7, ((2, 1, 0, 4, 5, 6, 3), (2, 1, 0, 4, 5, 6, 3), (2, 3, 0, 6, 1, 5, 4), (2, 5, 0, 3, 6, 4, 1), (2, 6, 0, 1, 4, 3, 5), (2, 3, 0, 6, 1, 5, 4), (2, 4, 0, 5, 3, 1, 6))),
    (5, ((0, 2, 0, 4, 0), (1, 1, 1, 1, 1), (3, 4, 2, 2, 2), (4, 3, 4, 3, 3), (4, 4, 4, 4, 4))),
    (6, ((0, 0, 3, 0, 5, 0), (2, 1, 1, 1, 1, 1), (3, 4, 2, 2, 2, 2), (4, 4, 5, 3, 3, 3), (4, 4, 4, 4, 4, 4), (3, 3, 3, 5, 5, 5))),
    (5, ((0, 2, 0, 0, 3), (3, 1, 3, 1, 3), (2, 0, 2, 4, 2), (3, 3, 3, 3, 3), (4, 0, 4, 2, 4))),
    (6, ((0, 5, 3, 0, 5, 0), (2, 1, 1, 1, 1, 2), (3, 4, 2, 2, 2, 3), (3, 4, 3, 3, 3, 3), (4, 3, 3, 4, 4, 3), (5, 0, 0, 5, 5, 5))),
    (6, ((0, 2, 0, 5, 5, 0), (3, 1, 1, 1, 1, 4), (2, 5, 2, 4, 2, 2), (4, 3, 3, 3, 3, 4), (2, 2, 4, 4, 4, 4), (5, 5, 5, 5, 5, 5))),
    (7, ((2, 1, 0, 5, 3, 4, 6), (4, 1, 3, 6, 5, 0, 2), (2, 6, 0, 1, 4, 5, 3), (4, 2, 6, 3, 5, 0, 1), (5, 2, 6, 0, 4, 3, 1), (3, 2, 6, 4, 0, 5, 1), (4, 3, 1, 2, 5, 0, 6))),
    (6, ((0, 2, 1, 5, 3, 4), (4, 2, 1, 3, 5, 0), (3, 2, 1, 4, 0, 5), (4, 2, 1, 3, 5, 0), (5, 2, 1, 0, 4, 3), (3, 2, 1, 4, 0, 5))),
    (5, ((3, 2, 0, 3, 2), (0, 4, 1, 1, 0), (2, 3, 2, 2, 2), (2, 2, 3, 3, 3), (4, 2, 4, 4, 2))),
    (6, ((3, 4, 1, 0, 5, 2), (2, 1, 3, 4, 0, 5), (5, 0, 4, 1, 2, 3), (0, 2, 5, 3, 1, 4), (1, 3, 2, 5, 4, 0), (4, 5, 0, 2, 3, 1))),
    (6, ((1, 3, 0, 4, 5, 2), (2, 0, 5, 1, 3, 4), (2, 3, 5, 1, 0, 4), (1, 3, 0, 4, 5, 2), (1, 0, 5, 2, 3, 4), (4, 0, 3, 1, 5, 2))),
    (6, ((1, 4, 3, 5, 2, 0), (2, 3, 4, 5, 1, 0), (5, 0, 4, 2, 1, 3), (1, 4, 3, 5, 2, 0), (5, 4, 0, 1, 2, 3), (5, 0, 4, 2, 1, 3))),
    (5, ((4, 2, 3, 1, 0), (3, 4, 0, 2, 1), (1, 3, 4, 0, 2), (2, 0, 1, 4, 3), (0, 1, 2, 3, 4))),
    (6, ((1, 5, 5, 2, 0, 0), (2, 5, 4, 1, 0, 0), (2, 4, 4, 1, 3, 3), (2, 4, 4, 2, 0, 0), (2, 4, 4, 2, 3, 0), (1, 4, 4, 1, 0, 0))),
    (5, ((2, 2, 4, 2, 4), (3, 3, 3, 3, 3), (0, 0, 4, 4, 0), (4, 1, 4, 1, 1), (2, 3, 2, 2, 0))),
    (6, ((1, 5, 1, 5, 1, 5), (2, 0, 2, 0, 2, 0), (3, 1, 3, 1, 3, 1), (4, 2, 4, 2, 4, 2), (5, 3, 5, 3, 5, 3), (0, 4, 0, 4, 0, 4))),
    (6, ((2, 2, 2, 4, 4, 4), (3, 1, 1, 3, 3, 1), (0, 5, 0, 0, 5, 5), (3, 1, 1, 3, 3, 1), (0, 5, 0, 0, 5, 5), (2, 2, 2, 4, 4, 4))),
    (6, ((2, 0, 4, 4, 0, 2), (2, 5, 1, 1, 5, 2), (3, 0, 1, 1, 0, 3), (2, 5, 4, 4, 5, 2), (3, 0, 4, 4, 0, 3), (3, 5, 1, 1, 5, 3))),
    (5, ((0, 1, 4, 4, 0), (2, 1, 4, 4, 1), (0, 3, 4, 4, 0), (0, 1, 4, 4, 1), (2, 3, 4, 4, 0))),
    (7, ((2, 1, 4, 6, 0, 5, 3), (3, 1, 6, 4, 5, 2, 0), (2, 1, 4, 3, 0, 6, 5), (2, 1, 4, 3, 0, 5, 6), (2, 1, 4, 5, 0, 3, 6), (2, 1, 4, 3, 0, 5, 6), (2, 1, 4, 3, 0, 5, 6))),
    (6, ((2, 3, 5, 0, 1, 4), (2, 5, 3, 4, 1, 0), (2, 5, 3, 4, 1, 0), (1, 5, 3, 0, 2, 4), (2, 3, 5, 0, 1, 4), (1, 5, 3, 0, 2, 4))),
    (6, ((1, 5, 4, 2, 0, 3), (2, 5, 4, 1, 3, 0), (2, 5, 4, 1, 3, 0), (1, 5, 4, 2, 0, 3), (1, 4, 5, 2, 3, 0), (1, 4, 5, 2, 3, 0))),
    (5, ((2, 2, 2, 4, 2), (4, 3, 3, 3, 3), (0, 4, 0, 0, 0), (1, 1, 4, 1, 1), (4, 4, 4, 4, 4))),
    (6, ((0, 2, 3, 5, 5, 2), (4, 4, 4, 4, 4, 4), (5, 3, 2, 0, 0, 3), (2, 0, 5, 3, 3, 0), (1, 1, 1, 1, 1, 1), (3, 5, 0, 2, 2, 5))),
    (5, ((1, 2, 2, 1, 2), (3, 3, 4, 0, 4), (3, 3, 3, 0, 3), (3, 3, 2, 1, 2), (1, 1, 1, 1, 1))),
    (5, ((0, 3, 3, 2, 2), (2, 4, 1, 2, 1), (0, 4, 3, 2, 4), (0, 3, 3, 2, 1), (3, 4, 3, 3, 1))),
    (6, ((3, 2, 1, 4, 3, 4), (2, 2, 0, 0, 5, 4), (3, 2, 1, 0, 5, 4), (2, 2, 0, 0, 5, 4), (3, 2, 1, 0, 5, 4), (3, 2, 1, 4, 3, 4))),
    (5, ((1, 2, 1, 4, 3), (3, 2, 1, 0, 0), (1, 2, 1, 4, 3), (4, 0, 1, 4, 0), (3, 0, 1, 0, 3))),
    (5, ((1, 0, 3, 2, 1), (2, 4, 0, 4, 1), (2, 0, 0, 4, 3), (2, 4, 3, 2, 1), (1, 0, 3, 4, 3))),
    (6, ((2, 3, 4, 1, 2, 4), (2, 3, 3, 1, 0, 4), (4, 3, 0, 1, 0, 4), (2, 3, 4, 1, 2, 4), (2, 3, 0, 2, 5, 4), (4, 3, 4, 1, 0, 4))),
    (6, ((2, 3, 5, 1, 5, 2), (5, 3, 3, 1, 5, 0), (5, 3, 0, 1, 5, 0), (1, 3, 5, 1, 5, 2), (5, 3, 5, 1, 5, 0), (2, 0, 0, 2, 5, 4))),
    (5, ((1, 2, 0, 4, 3), (0, 4, 3, 1, 2), (4, 3, 2, 0, 1), (2, 0, 1, 3, 4), (3, 1, 4, 2, 0))),
    (5, ((3, 2, 2, 3, 3), (0, 3, 3, 3, 0), (4, 3, 3, 3, 4), (4, 2, 1, 3, 0), (3, 1, 1, 3, 3))),
    (5, ((3, 2, 3, 3, 2), (4, 3, 4, 3, 3), (1, 1, 3, 3, 3), (1, 0, 4, 3, 2), (3, 0, 3, 3, 3))),
    (6, ((1, 5, 0, 4, 3, 2), (2, 5, 0, 4, 1, 3), (3, 0, 4, 5, 2, 1), (1, 4, 5, 0, 3, 2), (3, 0, 4, 5, 2, 1), (2, 4, 5, 0, 1, 3))),
    (5, ((1, 2, 1, 0, 2), (3, 1, 4, 0, 2), (1, 1, 1, 0, 2), (3, 2, 1, 1, 1), (3, 1, 4, 0, 1))),
    (5, ((1, 4, 1, 4, 4), (2, 1, 1, 2, 1), (3, 3, 1, 3, 0), (2, 2, 2, 1, 2), (0, 0, 1, 1, 1))),
    (5, ((0, 2, 0, 0, 3), (3, 4, 4, 1, 4), (3, 1, 3, 3, 3), (2, 2, 2, 2, 3), (2, 1, 4, 1, 1))),
    (5, ((2, 3, 3, 2, 0), (1, 2, 4, 4, 2), (2, 2, 2, 2, 2), (2, 3, 0, 2, 0), (1, 3, 1, 4, 2))),
    (5, ((2, 2, 1, 1, 0), (3, 2, 0, 1, 0), (2, 2, 2, 2, 2), (3, 4, 4, 2, 2), (3, 2, 3, 2, 2))),
    (5, ((1, 4, 4, 1, 4), (2, 4, 4, 1, 4), (2, 3, 2, 1, 2), (2, 3, 2, 1, 2), (1, 0, 0, 1, 1))),
    (5, ((1, 2, 3, 2, 1), (0, 4, 0, 0, 0), (3, 0, 3, 0, 3), (2, 0, 0, 2, 2), (1, 1, 1, 1, 1))),
    (6, ((1, 3, 3, 3, 1, 3), (4, 2, 4, 0, 2, 4), (1, 4, 1, 1, 1, 4), (5, 0, 5, 0, 5, 5), (1, 2, 1, 5, 5, 1), (3, 4, 4, 4, 4, 3))),
    (6, ((2, 2, 2, 2, 2, 2), (3, 3, 3, 4, 3, 4), (5, 0, 0, 0, 5, 0), (1, 1, 1, 1, 1, 1), (5, 5, 5, 1, 5, 1), (2, 4, 4, 4, 2, 4))),
    (5, ((1, 2, 0, 4, 3), (2, 4, 3, 0, 1), (3, 0, 2, 1, 4), (0, 1, 4, 3, 2), (4, 3, 1, 2, 0))),
    (5, ((4, 2, 3, 3, 0), (3, 2, 1, 3, 0), (4, 2, 1, 3, 3), (4, 2, 1, 3, 0), (4, 3, 1, 3, 0))),
    (5, ((1, 2, 4, 3, 0), (2, 1, 0, 4, 3), (3, 0, 1, 2, 4), (0, 4, 3, 1, 2), (4, 3, 2, 0, 1))),
    (6, ((1, 1, 5, 1, 5, 1), (2, 4, 4, 2, 4, 4), (3, 0, 3, 3, 3, 0), (5, 5, 1, 5, 1, 5), (0, 3, 0, 0, 0, 3), (4, 2, 2, 4, 2, 2))),
    (6, ((1, 4, 1, 1, 4, 1), (2, 2, 5, 2, 2, 5), (3, 0, 0, 3, 0, 0), (4, 1, 4, 4, 1, 4), (5, 5, 2, 5, 5, 2), (0, 3, 3, 0, 3, 3))),
    (7, ((3, 2, 3, 3, 3, 3, 3), (1, 1, 1, 1, 1, 1, 1), (6, 4, 2, 2, 5, 2, 2), (4, 6, 4, 4, 4, 4, 4), (0, 5, 0, 0, 0, 0, 0), (5, 3, 5, 6, 2, 5, 5), (2, 0, 6, 5, 6, 6, 6))),
    (7, ((2, 4, 2, 4, 5, 1, 4), (5, 1, 6, 2, 0, 4, 3), (0, 3, 0, 6, 3, 3, 1), (3, 6, 1, 3, 6, 6, 2), (1, 5, 4, 5, 4, 0, 5), (4, 0, 5, 0, 1, 5, 0), (6, 2, 3, 1, 2, 2, 6))),
    (6, ((2, 4, 0, 2, 4, 0), (2, 1, 3, 2, 1, 3), (2, 1, 0, 2, 1, 0), (5, 1, 3, 5, 1, 3), (5, 4, 0, 5, 4, 0), (5, 4, 3, 5, 4, 3))),
    (6, ((1, 2, 2, 2, 1, 2), (4, 4, 4, 3, 4, 3), (4, 4, 3, 3, 3, 3), (0, 0, 5, 5, 0, 0), (0, 0, 5, 0, 0, 0), (1, 2, 2, 2, 1, 2))),
    (6, ((2, 1, 2, 1, 1, 2), (3, 3, 5, 5, 5, 3), (3, 3, 5, 5, 5, 3), (0, 4, 0, 0, 4, 4), (2, 1, 2, 1, 1, 2), (0, 4, 0, 0, 4, 4))),
    (6, ((1, 2, 3, 4, 5, 0), (5, 0, 1, 2, 3, 4), (1, 2, 3, 4, 5, 0), (5, 0, 1, 2, 3, 4), (1, 2, 3, 4, 5, 0), (5, 0, 1, 2, 3, 4))),
    (6, ((1, 2, 4, 1, 4, 4), (3, 0, 3, 3, 0, 3), (5, 5, 5, 0, 5, 5), (4, 1, 1, 4, 1, 1), (0, 3, 0, 5, 3, 0), (2, 4, 2, 2, 2, 2))),
    (6, ((1, 2, 5, 1, 5, 5), (4, 4, 0, 4, 4, 0), (3, 3, 4, 3, 0, 4), (5, 5, 2, 5, 2, 2), (2, 1, 1, 2, 1, 1), (0, 0, 3, 0, 3, 3))),
    (5, ((2, 2, 4, 3, 3), (4, 2, 3, 2, 3), (4, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 2, 2, 3, 4))),
    (5, ((0, 2, 2, 4, 3), (3, 1, 3, 3, 4), (0, 1, 2, 4, 3), (0, 1, 2, 3, 4), (2, 1, 3, 3, 4))),
    (6, ((0, 1, 1, 3, 4, 5), (5, 1, 2, 4, 5, 5), (3, 1, 2, 5, 5, 0), (0, 1, 1, 3, 4, 5), (5, 2, 1, 3, 4, 5), (0, 2, 1, 3, 4, 5))),
    (6, ((0, 2, 5, 5, 5, 5), (5, 1, 5, 4, 5, 5), (3, 1, 2, 5, 5, 5), (0, 1, 5, 3, 5, 5), (5, 1, 5, 3, 4, 5), (0, 1, 2, 3, 4, 5))),
    (5, ((0, 1, 3, 4, 4), (2, 1, 2, 4, 4), (0, 1, 2, 4, 4), (0, 1, 2, 3, 4), (2, 1, 2, 3, 4))),
    (5, ((0, 1, 2, 4, 4), (2, 1, 3, 4, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (2, 0, 2, 3, 4))),
    (5, ((0, 2, 3, 2, 2), (2, 1, 4, 2, 4), (0, 1, 2, 3, 4), (4, 1, 2, 3, 4), (0, 3, 2, 3, 4))),
    (5, ((0, 1, 3, 2, 4), (2, 1, 4, 3, 2), (0, 1, 2, 3, 4), (4, 1, 2, 3, 4), (0, 1, 2, 3, 4))),
    (5, ((0, 2, 2, 3, 4), (3, 1, 3, 0, 0), (0, 1, 2, 4, 3), (0, 1, 2, 3, 4), (2, 2, 2, 3, 4))),
    (6, ((0, 2, 5, 4, 3, 2), (1, 1, 1, 1, 1, 1), (4, 3, 2, 5, 0, 3), (2, 4, 0, 3, 5, 4), (5, 0, 3, 2, 4, 0), (3, 5, 4, 0, 2, 5))),
    (6, ((0, 3, 3, 3, 4, 5), (5, 1, 3, 3, 3, 5), (4, 3, 2, 3, 4, 3), (0, 1, 2, 3, 4, 5), (0, 5, 2, 3, 4, 5), (0, 1, 3, 3, 4, 5))),
    (5, ((4, 2, 2, 2, 4), (3, 4, 3, 3, 4), (0, 0, 4, 0, 4), (1, 1, 1, 4, 4), (0, 1, 2, 3, 4))),
    (5, ((0, 4, 3, 3, 4), (2, 1, 2, 3, 4), (0, 4, 2, 4, 1), (4, 1, 2, 3, 4), (0, 1, 2, 3, 4))),
    (6, ((0, 4, 3, 3, 4, 2), (2, 1, 2, 4, 4, 2), (0, 1, 2, 4, 0, 5), (4, 1, 2, 3, 0, 5), (5, 1, 2, 3, 4, 2), (0, 1, 3, 4, 0, 5))),
    (5, ((1, 3, 4, 1, 2), (2, 4, 3, 2, 1), (4, 2, 1, 4, 3), (1, 0, 4, 4, 3), (0, 1, 2, 3, 4))),
    (5, ((1, 4, 3, 2, 0), (2, 0, 1, 4, 3), (3, 2, 4, 0, 1), (0, 1, 2, 3, 4), (4, 3, 0, 1, 2))),
    (5, ((0, 0, 0, 4, 4), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3), (1, 1, 1, 1, 1), (4, 4, 4, 0, 0))),
    (7, ((0, 2, 6, 1, 5, 3, 4), (5, 5, 1, 6, 0, 5, 5), (4, 3, 4, 4, 4, 2, 0), (2, 0, 2, 2, 2, 4, 3), (3, 4, 3, 3, 3, 0, 2), (6, 6, 0, 5, 1, 6, 6), (1, 1, 5, 0, 6, 1, 1))),
    (6, ((2, 4, 2, 0, 2, 2), (3, 3, 3, 3, 3, 3), (4, 2, 4, 4, 4, 0), (5, 5, 5, 5, 5, 5), (0, 0, 0, 2, 0, 4), (1, 1, 1, 1, 1, 1))),
    (5, ((1, 2, 2, 1, 1), (2, 2, 2, 2, 4), (0, 4, 4, 3, 4), (1, 1, 2, 1, 1), (0, 1, 3, 3, 3))),
    (5, ((0, 0, 4, 0, 0), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3), (1, 1, 1, 1, 1), (4, 4, 0, 4, 4))),
    (5, ((0, 3, 0, 0, 0), (1, 1, 1, 2, 1), (2, 2, 2, 1, 2), (3, 0, 4, 3, 3), (4, 4, 3, 4, 4))),
    (6, ((1, 2, 2, 1, 1, 1), (5, 5, 5, 5, 4, 4), (4, 4, 4, 4, 5, 5), (2, 1, 1, 2, 2, 2), (3, 0, 0, 3, 0, 0), (0, 3, 3, 0, 3, 3))),
    (5, ((2, 0, 2, 2, 2), (1, 1, 1, 1, 1), (3, 3, 3, 3, 3), (0, 4, 0, 0, 0), (4, 2, 4, 4, 4))),
    (5, ((1, 2, 2, 2, 2), (4, 4, 4, 4, 4), (4, 4, 4, 4, 4), (1, 1, 2, 1, 1), (0, 3, 3, 3, 3))),
    (6, ((0, 1, 0, 3, 4, 5), (2, 5, 2, 5, 5, 5), (2, 1, 2, 3, 4, 5), (0, 1, 2, 4, 4, 4), (0, 5, 2, 5, 5, 5), (0, 3, 2, 3, 3, 3))),
    (6, ((2, 3, 2, 3, 2, 2), (2, 1, 2, 1, 4, 5), (5, 1, 5, 3, 5, 5), (0, 3, 2, 3, 4, 5), (2, 1, 2, 3, 2, 2), (0, 1, 4, 3, 4, 4))),
    (6, ((0, 1, 0, 3, 4, 5), (2, 4, 0, 4, 4, 4), (2, 1, 2, 3, 4, 5), (0, 1, 2, 5, 5, 5), (0, 3, 2, 3, 3, 3), (0, 4, 2, 4, 4, 4))),
    (7, ((5, 2, 3, 3, 5, 5, 5), (4, 1, 3, 3, 4, 5, 6), (0, 2, 2, 2, 4, 5, 6), (0, 1, 3, 3, 4, 5, 6), (5, 1, 2, 3, 5, 5, 5), (6, 1, 2, 3, 6, 6, 6), (0, 1, 2, 3, 4, 4, 4))),
    (5, ((3, 2, 2, 3, 3), (1, 1, 1, 1, 1), (0, 2, 2, 3, 4), (4, 2, 2, 4, 4), (0, 2, 2, 0, 0))),
    (6, ((3, 3, 2, 3, 3, 3), (0, 2, 2, 2, 2, 2), (4, 3, 4, 3, 4, 4), (1, 1, 5, 1, 4, 5), (0, 1, 0, 0, 0, 5), (0, 2, 2, 2, 2, 2))),
    (6, ((1, 2, 3, 2, 5, 2), (4, 3, 2, 3, 0, 3), (3, 4, 5, 4, 1, 4), (0, 5, 4, 5, 2, 5), (5, 0, 1, 0, 3, 0), (2, 1, 0, 1, 4, 1))),
    (5, ((3, 1, 3, 3, 3), (2, 4, 2, 4, 4), (0, 0, 0, 0, 0), (4, 4, 2, 2, 4), (0, 0, 0, 0, 0))),
    (6, ((1, 2, 2, 3, 1, 5), (2, 2, 3, 3, 4, 5), (0, 3, 5, 5, 4, 5), (0, 1, 5, 5, 4, 4), (1, 1, 2, 3, 1, 0), (0, 1, 2, 4, 0, 0))),
    (6, ((0, 4, 1, 3, 4, 1), (2, 1, 5, 5, 4, 5), (3, 0, 2, 3, 0, 5), (0, 0, 2, 3, 0, 0), (0, 1, 1, 2, 4, 5), (2, 1, 2, 2, 4, 5))),
    (8, ((1, 5, 1, 3, 7, 5, 6, 7), (2, 6, 3, 3, 2, 7, 6, 3), (4, 5, 2, 3, 7, 7, 7, 7), (0, 1, 2, 3, 2, 7, 6, 2), (4, 6, 1, 6, 4, 5, 6, 7), (0, 6, 3, 6, 4, 5, 6, 3), (0, 1, 3, 3, 4, 5, 6, 3), (0, 5, 2, 5, 4, 4, 5, 7))),
    (5, ((1, 2, 4, 3, 0), (4, 3, 2, 0, 1), (3, 1, 0, 4, 2), (0, 4, 1, 2, 3), (2, 0, 3, 1, 4))),
    (5, ((1, 0, 2, 4, 3), (2, 3, 0, 1, 4), (3, 1, 4, 0, 2), (0, 4, 3, 2, 1), (4, 2, 1, 3, 0))),
    (5, ((0, 3, 3, 4, 4), (2, 1, 3, 3, 4), (0, 3, 2, 4, 4), (0, 1, 2, 3, 4), (2, 1, 2, 3, 4))),
    (7, ((1, 2, 3, 6, 6, 2, 6), (4, 6, 2, 3, 6, 5, 6), (0, 1, 5, 6, 4, 6, 6), (4, 1, 3, 6, 4, 4, 6), (4, 6, 2, 3, 6, 5, 6), (0, 1, 5, 6, 4, 6, 6), (0, 1, 2, 3, 4, 5, 6))),
    (5, ((1, 4, 3, 4, 4), (2, 4, 3, 3, 4), (1, 4, 3, 4, 4), (1, 1, 0, 4, 4), (0, 1, 2, 3, 4))),
    (6, ((0, 4, 3, 3, 4, 5), (2, 1, 5, 3, 4, 2), (5, 4, 2, 3, 4, 5), (4, 4, 2, 3, 5, 5), (5, 1, 5, 3, 4, 5), (0, 1, 2, 3, 4, 5))),
    (5, ((0, 3, 0, 0, 2), (4, 1, 1, 1, 1), (2, 2, 2, 2, 0), (3, 0, 4, 3, 3), (1, 4, 3, 4, 4))),
    (5, ((4, 1, 4, 4, 4), (1, 4, 2, 2, 2), (0, 0, 3, 3, 3), (1, 1, 4, 4, 4), (2, 2, 2, 2, 2))),
    (6, ((1, 1, 4, 1, 1, 4), (2, 5, 5, 2, 5, 5), (0, 3, 0, 0, 3, 0), (4, 4, 1, 4, 4, 1), (5, 2, 2, 5, 2, 2), (3, 0, 3, 3, 0, 3))),
    (7, ((1, 5, 5, 3, 5, 5, 5), (2, 2, 2, 2, 2, 2, 6), (3, 3, 3, 3, 4, 5, 3), (6, 1, 6, 6, 6, 6, 6), (1, 1, 1, 3, 1, 5, 1), (6, 6, 6, 6, 6, 6, 6), (0, 4, 2, 4, 4, 4, 4))),
    (8, ((0, 2, 3, 5, 0, 5, 6, 7), (4, 1, 5, 1, 4, 5, 1, 5), (4, 6, 2, 6, 4, 2, 6, 2), (4, 7, 7, 3, 4, 7, 3, 7), (4, 1, 2, 3, 4, 5, 6, 7), (0, 1, 5, 5, 4, 5, 6, 5), (0, 6, 2, 6, 4, 5, 6, 2), (0, 7, 7, 3, 4, 7, 3, 7))),
    (6, ((0, 2, 5, 0, 4, 5), (3, 1, 3, 3, 1, 3), (2, 4, 2, 2, 4, 2), (3, 1, 3, 3, 1, 3), (0, 4, 2, 0, 4, 5), (0, 4, 5, 0, 4, 5))),
    (7, ((0, 2, 2, 0, 0, 0, 0), (3, 3, 3, 3, 3, 3, 3), (0, 2, 2, 4, 4, 0, 0), (5, 5, 5, 5, 5, 5, 5), (4, 4, 2, 4, 4, 4, 4), (6, 1, 6, 6, 6, 6, 6), (3, 3, 3, 3, 3, 3, 3))),
    (5, ((1, 2, 2, 1, 2), (4, 2, 2, 4, 4), (4, 3, 2, 3, 4), (4, 1, 2, 3, 4), (0, 3, 2, 3, 4))),
    (5, ((1, 4, 2, 3, 0), (2, 1, 3, 4, 2), (0, 3, 1, 2, 4), (0, 2, 4, 3, 1), (3, 4, 2, 1, 3))),
    (5, ((1, 2, 2, 1, 4), (3, 1, 2, 4, 0), (3, 1, 2, 4, 0), (0, 2, 2, 1, 2), (1, 1, 2, 3, 2))),
    (6, ((1, 1, 1, 3, 3, 5), (2, 4, 2, 3, 4, 4), (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5), (0, 5, 2, 0, 0, 3), (0, 1, 2, 3, 4, 5))),
    (6, ((1, 2, 4, 4, 5, 2), (5, 3, 2, 3, 5, 3), (5, 5, 3, 0, 0, 4), (0, 5, 4, 0, 0, 5), (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))),
    (5, ((0, 2, 0, 4, 0), (3, 3, 3, 3, 3), (2, 4, 2, 0, 2), (1, 1, 1, 1, 1), (4, 0, 4, 2, 4))),
    (5, ((1, 1, 3, 3, 3), (2, 2, 2, 2, 2), (4, 4, 4, 4, 4), (2, 2, 2, 2, 2), (0, 0, 0, 0, 0))),
    (6, ((3, 3, 4, 3, 4, 4), (0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1), (2, 5, 2, 5, 5, 5), (5, 5, 2, 5, 5, 5), (1, 1, 1, 1, 1, 1))),
    (5, ((0, 2, 1, 4, 1), (2, 1, 2, 4, 4), (3, 1, 2, 4, 1), (4, 2, 0, 3, 4), (0, 2, 1, 3, 4))),
    (5, ((0, 3, 4, 3, 4), (3, 1, 2, 3, 4), (4, 1, 2, 1, 4), (0, 1, 1, 3, 1), (0, 1, 2, 1, 4))),
    (5, ((0, 1, 4, 3, 4), (0, 1, 3, 3, 4), (3, 4, 2, 3, 4), (0, 1, 2, 3, 2), (0, 1, 2, 2, 4))),
    (5, ((0, 4, 2, 3, 4), (2, 1, 2, 2, 3), (3, 4, 2, 0, 0), (0, 4, 0, 3, 4), (3, 1, 1, 3, 4))),
    (5, ((0, 3, 3, 2, 2), (2, 1, 2, 2, 4), (4, 3, 2, 3, 4), (4, 1, 2, 3, 2), (0, 3, 2, 3, 4))),
    (5, ((0, 2, 2, 3, 3), (2, 1, 2, 3, 3), (3, 4, 2, 3, 4), (0, 4, 0, 3, 4), (3, 1, 1, 1, 4))),
    (6, ((0, 5, 3, 2, 4, 2), (5, 2, 2, 4, 3, 0), (3, 1, 2, 0, 3, 0), (2, 4, 0, 3, 2, 5), (0, 5, 3, 2, 0, 2), (2, 4, 0, 3, 2, 3))),
    (5, ((4, 4, 4, 4, 4), (2, 4, 2, 3, 4), (3, 1, 4, 3, 4), (4, 1, 2, 4, 4), (0, 1, 2, 3, 4))),
    (5, ((2, 1, 2, 2, 4), (0, 4, 3, 3, 4), (0, 4, 4, 3, 4), (4, 1, 2, 4, 4), (0, 1, 2, 3, 4))),
    (6, ((3, 3, 3, 3, 3, 5), (2, 5, 2, 2, 2, 5), (1, 1, 5, 1, 1, 5), (0, 4, 4, 5, 4, 5), (5, 3, 3, 3, 5, 5), (0, 1, 2, 3, 4, 5))),
    (6, ((3, 3, 2, 3, 5, 5), (4, 2, 2, 3, 4, 5), (0, 1, 5, 4, 4, 5), (0, 1, 5, 5, 4, 5), (1, 1, 2, 3, 5, 5), (0, 1, 2, 3, 4, 5))),
    (5, ((2, 2, 2, 2, 2), (3, 3, 2, 3, 2), (0, 1, 2, 3, 4), (4, 1, 2, 2, 4), (3, 2, 2, 3, 2))),
    (5, ((1, 3, 3, 1, 3), (4, 0, 4, 0, 4), (0, 1, 2, 3, 4), (4, 2, 2, 2, 4), (2, 3, 2, 3, 2))),
    (5, ((1, 1, 3, 4, 1), (2, 1, 1, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1), (4, 1, 1, 1, 1))),
    (5, ((1, 1, 4, 4, 1), (2, 1, 3, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1))),
    (5, ((2, 3, 2, 0, 0), (4, 1, 1, 4, 1), (2, 4, 2, 2, 2), (4, 3, 4, 3, 3), (4, 4, 4, 4, 4))),
    (6, ((5, 1, 2, 0, 5, 4), (2, 0, 0, 3, 1, 5), (1, 0, 0, 5, 2, 3), (4, 5, 3, 1, 0, 1), (5, 2, 1, 4, 5, 0), (0, 3, 5, 1, 4, 1))),
    (7, ((1, 2, 1, 0, 3, 0, 0), (1, 5, 5, 1, 3, 2, 1), (0, 1, 4, 4, 3, 5, 3), (1, 5, 4, 6, 2, 0, 3), (2, 2, 3, 2, 2, 2, 3), (2, 5, 0, 5, 3, 0, 5), (1, 5, 3, 3, 3, 0, 3))),
    (5, ((0, 2, 4, 4, 1), (4, 1, 0, 0, 2), (1, 4, 3, 3, 0), (1, 4, 3, 3, 0), (2, 0, 1, 1, 4))),
    (5, ((2, 4, 4, 4, 4), (0, 3, 3, 3, 3), (0, 0, 0, 0, 0), (3, 3, 3, 3, 3), (0, 0, 0, 0, 0))),
    (5, ((2, 3, 3, 2, 2), (2, 1, 1, 2, 2), (4, 3, 3, 4, 4), (2, 1, 1, 2, 2), (4, 3, 3, 4, 4))),
    (6, ((4, 1, 4, 3, 0, 2), (3, 2, 1, 2, 4, 5), (4, 3, 4, 1, 2, 0), (1, 2, 3, 2, 5, 4), (2, 5, 0, 4, 3, 3), (0, 4, 2, 5, 3, 3))),
    (5, ((1, 2, 1, 1, 2), (2, 3, 3, 2, 4), (2, 3, 4, 1, 4), (1, 2, 1, 1, 2), (1, 2, 4, 2, 2))),
    (5, ((4, 2, 2, 3, 4), (2, 3, 2, 3, 4), (3, 3, 2, 3, 4), (2, 3, 2, 3, 4), (4, 2, 2, 3, 4))),
    (5, ((4, 2, 2, 3, 4), (3, 4, 2, 3, 4), (3, 3, 2, 3, 4), (4, 2, 2, 3, 4), (4, 4, 2, 3, 4))),
    (6, ((2, 4, 2, 4, 3, 3), (5, 3, 5, 3, 0, 2), (2, 4, 2, 4, 3, 3), (4, 3, 4, 3, 2, 0), (3, 0, 3, 2, 4, 4), (1, 2, 1, 0, 5, 4))),
    (5, ((2, 3, 2, 2, 2), (4, 4, 4, 4, 4), (2, 3, 2, 0, 2), (2, 3, 2, 2, 2), (4, 4, 4, 4, 4))),
    (5, ((2, 3, 2, 2, 2), (4, 4, 4, 4, 4), (2, 0, 2, 2, 2), (2, 3, 0, 2, 2), (4, 4, 4, 4, 4))),
    (5, ((2, 4, 2, 2, 4), (3, 4, 3, 0, 4), (2, 4, 2, 0, 4), (2, 4, 2, 2, 4), (2, 4, 2, 2, 4))),
    (5, ((2, 4, 3, 2, 4), (0, 4, 3, 0, 4), (2, 4, 2, 2, 4), (2, 4, 2, 2, 4), (2, 4, 2, 2, 4))),
    (5, ((4, 2, 4, 2, 4), (3, 4, 3, 4, 4), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3), (4, 4, 4, 4, 4))),
    (5, ((1, 2, 2, 1, 1), (2, 3, 3, 2, 2), (1, 3, 4, 1, 2), (1, 2, 1, 1, 2), (2, 2, 2, 2, 2))),
    (5, ((2, 2, 2, 4, 2), (3, 4, 3, 2, 4), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3), (4, 4, 4, 4, 4))),
    (6, ((1, 2, 3, 5, 2, 1), (5, 4, 5, 1, 4, 2), (1, 5, 3, 2, 2, 1), (5, 1, 2, 3, 3, 5), (2, 4, 2, 3, 4, 5), (3, 2, 1, 5, 5, 3))),
    (5, ((1, 3, 1, 3, 1), (2, 2, 4, 2, 4), (1, 3, 1, 3, 1), (1, 3, 1, 3, 1), (2, 2, 4, 2, 4))),
    (5, ((2, 3, 2, 1, 1), (1, 4, 2, 1, 1), (2, 3, 2, 1, 1), (2, 3, 2, 1, 1), (2, 3, 2, 1, 1))),
    (5, ((0, 0, 0, 0, 0), (2, 0, 0, 0, 0), (4, 3, 0, 1, 4), (0, 4, 0, 0, 4), (0, 0, 0, 0, 0))),
    (5, ((0, 0, 0, 0, 0), (2, 0, 0, 0, 4), (0, 3, 0, 0, 4), (0, 4, 0, 0, 0), (0, 0, 0, 0, 0))),
    (5, ((2, 3, 2, 2, 2), (4, 2, 2, 2, 4), (2, 2, 2, 2, 2), (2, 1, 2, 2, 2), (2, 2, 2, 2, 2))),
    (5, ((0, 2, 3, 4, 0), (1, 1, 1, 1, 3), (4, 4, 2, 4, 2), (3, 0, 0, 3, 3), (1, 4, 1, 4, 4))),
    (5, ((2, 4, 2, 4, 4), (3, 1, 4, 3, 4), (2, 1, 2, 4, 4), (0, 4, 2, 3, 4), (0, 1, 2, 3, 4))),
    (5, ((0, 2, 3, 0, 3), (4, 1, 4, 4, 1), (2, 4, 2, 4, 2), (4, 4, 4, 3, 3), (4, 4, 0, 0, 4))),
    (5, ((0, 2, 4, 0, 0), (3, 1, 3, 1, 0), (2, 0, 2, 0, 0), (3, 0, 3, 3, 0), (2, 2, 4, 2, 4))),
    (5, ((0, 2, 3, 0, 3), (4, 1, 4, 4, 1), (2, 2, 2, 0, 1), (2, 3, 3, 3, 1), (2, 2, 4, 4, 4))),
    (5, ((0, 3, 4, 0, 0), (3, 1, 1, 1, 1), (4, 2, 2, 1, 2), (3, 3, 1, 3, 1), (4, 4, 4, 1, 4))),
    (5, ((0, 3, 4, 0, 0), (4, 1, 3, 1, 1), (4, 4, 2, 2, 2), (3, 3, 3, 3, 1), (4, 4, 4, 0, 4))),
    (5, ((2, 0, 0, 4, 0), (1, 4, 4, 1, 1), (2, 3, 4, 2, 2), (4, 3, 3, 4, 3), (4, 4, 4, 4, 4))),
    (5, ((2, 3, 0, 4, 3), (2, 3, 1, 1, 2), (2, 2, 2, 2, 2), (2, 3, 3, 2, 3), (2, 3, 4, 4, 2))),
    (6, ((2, 3, 0, 1, 5, 0), (2, 5, 4, 1, 2, 1), (2, 3, 5, 1, 2, 2), (2, 3, 4, 5, 2, 3), (5, 3, 4, 1, 5, 4), (5, 5, 5, 5, 5, 5))),
    (6, ((2, 4, 0, 0, 1, 0), (5, 3, 1, 1, 1, 1), (2, 2, 5, 4, 2, 2), (3, 3, 5, 4, 3, 3), (5, 4, 4, 4, 5, 4), (5, 5, 5, 5, 5, 5))),
    (5, ((4, 2, 3, 4, 0), (4, 4, 1, 2, 1), (4, 2, 4, 2, 2), (4, 2, 3, 4, 3), (4, 4, 4, 4, 4))),
    (8, ((1, 4, 1, 3, 5, 3, 4, 5), (7, 5, 3, 3, 3, 3, 3, 3), (6, 4, 6, 3, 3, 3, 4, 5), (5, 3, 5, 3, 3, 3, 3, 3), (5, 3, 5, 3, 3, 3, 3, 3), (5, 3, 5, 3, 3, 3, 3, 3), (7, 5, 3, 3, 3, 3, 3, 3), (5, 3, 5, 3, 3, 3, 3, 3))),
    (5, ((3, 2, 3, 3, 2), (4, 2, 3, 3, 3), (3, 3, 3, 3, 3), (3, 3, 3, 3, 3), (3, 3, 3, 3, 3))),
    (5, ((3, 2, 3, 3, 2), (2, 4, 3, 3, 3), (3, 3, 3, 3, 3), (3, 3, 3, 3, 3), (3, 3, 3, 3, 3))),
    (5, ((1, 2, 4, 2, 0), (3, 4, 1, 1, 1), (3, 2, 4, 2, 2), (3, 3, 3, 4, 3), (3, 4, 4, 4, 4))),
    (5, ((1, 3, 0, 2, 3), (4, 0, 1, 4, 2), (4, 3, 2, 2, 2), (1, 3, 3, 2, 3), (4, 0, 4, 4, 2))),
    (5, ((4, 2, 3, 3, 3), (4, 3, 3, 3, 3), (4, 3, 3, 3, 3), (3, 3, 3, 3, 3), (3, 2, 3, 3, 3))),
    (6, ((3, 2, 3, 5, 5, 5), (4, 3, 5, 5, 5, 5), (5, 5, 5, 5, 5, 5), (5, 5, 5, 5, 5, 5), (3, 5, 5, 5, 5, 5), (5, 5, 5, 5, 5, 5))),
    (6, ((4, 2, 3, 3, 5, 3), (3, 3, 3, 3, 5, 3), (5, 3, 3, 3, 3, 3), (3, 3, 3, 3, 3, 3), (5, 3, 3, 3, 3, 3), (3, 3, 3, 3, 3, 3))),
    (5, ((1, 2, 4, 2, 0), (1, 2, 4, 2, 0), (3, 2, 4, 2, 0), (3, 2, 4, 2, 0), (3, 2, 4, 2, 0))),
    (6, ((2, 3, 4, 5, 5, 0), (1, 4, 4, 5, 5, 0), (2, 4, 4, 5, 5, 0), (1, 3, 3, 5, 5, 0), (2, 4, 4, 5, 5, 0), (2, 3, 4, 5, 5, 0))),
    (8, ((7, 3, 1, 3, 4, 3, 3, 3), (5, 3, 5, 4, 4, 4, 4, 3), (7, 6, 1, 4, 4, 3, 3, 6), (4, 4, 4, 4, 4, 4, 4, 4), (4, 4, 4, 4, 4, 4, 4, 4), (4, 4, 3, 4, 4, 4, 4, 4), (3, 4, 3, 4, 4, 4, 4, 4), (5, 4, 5, 4, 4, 4, 4, 4))),
    (7, ((2, 1, 3, 5, 4, 0, 6), (2, 1, 3, 5, 4, 0, 6), (2, 1, 3, 5, 4, 0, 6), (2, 4, 3, 5, 6, 0, 1), (2, 1, 3, 5, 4, 0, 6), (2, 4, 3, 5, 6, 0, 1), (2, 1, 3, 5, 4, 0, 6))),
    (5, ((2, 1, 0, 3, 4), (2, 1, 0, 3, 4), (2, 4, 0, 1, 3), (2, 1, 0, 3, 4), (2, 1, 0, 3, 4))),
    (5, ((1, 3, 3, 0, 3), (2, 2, 4, 4, 1), (2, 2, 2, 2, 2), (2, 3, 3, 3, 2), (2, 3, 3, 4, 4))),
    (5, ((2, 0, 1, 1, 2), (3, 3, 4, 4, 1), (3, 3, 2, 2, 2), (2, 2, 3, 3, 2), (4, 3, 0, 0, 3))),
    (5, ((1, 2, 4, 1, 0), (2, 1, 3, 2, 4), (3, 4, 2, 0, 1), (1, 2, 4, 1, 3), (4, 3, 1, 4, 2))),
    (5, ((1, 2, 0, 0, 3), (4, 1, 3, 2, 0), (2, 3, 1, 4, 2), (3, 4, 2, 3, 1), (0, 2, 4, 1, 4))),
    (6, ((0, 2, 5, 5, 0, 5), (4, 1, 2, 1, 4, 1), (4, 3, 2, 3, 4, 2), (4, 3, 2, 3, 4, 3), (4, 3, 2, 3, 4, 4), (0, 5, 5, 5, 5, 5))),
    (8, ((0, 4, 4, 4, 4, 0, 0, 0), (2, 1, 5, 7, 1, 5, 1, 7), (3, 6, 2, 7, 2, 2, 6, 7), (6, 6, 5, 3, 3, 5, 6, 3), (0, 4, 4, 4, 4, 4, 4, 4), (5, 6, 5, 3, 5, 5, 6, 3), (6, 6, 2, 7, 6, 5, 6, 7), (7, 6, 2, 7, 7, 2, 6, 7))),
    (7, ((0, 2, 5, 0, 4, 6, 2), (3, 2, 5, 3, 4, 1, 2), (0, 2, 5, 4, 4, 6, 2), (3, 2, 5, 3, 3, 6, 2), (0, 2, 5, 4, 4, 6, 2), (0, 2, 5, 0, 4, 1, 2), (0, 2, 5, 4, 4, 6, 2))),
    (6, ((1, 2, 0, 0, 1, 0), (1, 3, 1, 5, 5, 1), (1, 2, 2, 5, 1, 2), (5, 3, 3, 0, 0, 3), (2, 2, 4, 3, 0, 4), (5, 4, 5, 0, 5, 5))),
    (7, ((1, 2, 3, 5, 5, 0, 1), (4, 2, 3, 1, 5, 6, 1), (4, 2, 3, 5, 5, 2, 1), (4, 2, 3, 5, 5, 6, 3), (4, 2, 4, 1, 5, 6, 4), (4, 5, 3, 5, 5, 6, 1), (4, 2, 6, 5, 5, 6, 1))),
    (5, ((4, 1, 0, 2, 3), (1, 2, 0, 2, 1), (3, 2, 4, 2, 3), (3, 2, 4, 2, 3), (3, 2, 4, 2, 3))),
    (5, ((1, 3, 4, 0, 0), (1, 4, 3, 0, 0), (2, 4, 4, 0, 0), (2, 3, 3, 0, 0), (2, 4, 4, 0, 0))),
    (6, ((1, 2, 0, 5, 3, 4), (1, 4, 3, 5, 0, 2), (5, 4, 0, 1, 3, 2), (1, 2, 0, 5, 3, 4), (5, 4, 0, 1, 3, 2), (1, 4, 3, 5, 0, 2))),
    (5, ((0, 1, 2, 3, 4), (0, 1, 2, 4, 3), (3, 1, 2, 0, 4), (0, 1, 2, 3, 4), (1, 0, 2, 3, 4))),
    (5, ((2, 1, 3, 0, 4), (0, 1, 3, 4, 2), (2, 1, 3, 0, 4), (2, 1, 3, 0, 4), (2, 1, 3, 0, 4))),
    (6, ((1, 2, 5, 0, 3, 4), (4, 3, 0, 5, 2, 1), (3, 4, 1, 2, 5, 0), (4, 3, 0, 5, 2, 1), (5, 0, 3, 4, 1, 2), (4, 3, 0, 5, 2, 1))),
    (5, ((1, 2, 4, 3, 0), (0, 4, 1, 2, 3), (2, 0, 3, 1, 4), (4, 3, 2, 0, 1), (3, 1, 0, 4, 2))),
    (6, ((0, 2, 5, 4, 5, 0), (4, 1, 4, 4, 1, 1), (3, 5, 2, 2, 5, 2), (2, 2, 3, 3, 3, 3), (4, 2, 5, 5, 4, 4), (2, 2, 5, 5, 5, 5))),
    (5, ((1, 3, 3, 0, 2), (2, 3, 3, 4, 1), (2, 3, 3, 4, 2), (1, 3, 3, 4, 1), (2, 3, 3, 4, 2))),
    (5, ((0, 2, 0, 0, 2), (3, 1, 1, 1, 2), (2, 2, 2, 4, 2), (3, 2, 3, 3, 2), (4, 2, 4, 2, 4))),
    (5, ((0, 2, 0, 0, 2), (1, 1, 1, 4, 1), (2, 3, 2, 2, 2), (4, 3, 3, 3, 3), (1, 4, 4, 4, 4))),
    (8, ((1, 2, 4, 4, 0, 0, 0, 2), (4, 6, 4, 1, 6, 1, 1, 1), (1, 3, 2, 2, 7, 2, 3, 3), (1, 3, 3, 3, 7, 3, 3, 3), (4, 5, 5, 2, 4, 4, 4, 2), (5, 5, 5, 5, 5, 0, 7, 3), (6, 6, 4, 6, 6, 0, 6, 6), (1, 7, 4, 7, 6, 4, 7, 7))),
    (6, ((2, 0, 3, 0, 0, 2), (1, 0, 1, 1, 5, 0), (3, 2, 3, 4, 2, 2), (3, 3, 4, 4, 1, 3), (4, 5, 4, 1, 5, 4), (2, 0, 5, 5, 5, 0))),
    (5, ((1, 2, 1, 1, 0), (4, 4, 4, 1, 1), (3, 3, 3, 3, 2), (4, 3, 4, 4, 3), (4, 4, 4, 4, 4))),
    (7, ((1, 1, 0, 4, 1, 0, 0), (2, 6, 1, 6, 2, 1, 1), (3, 2, 5, 5, 2, 5, 2), (3, 2, 5, 5, 2, 5, 3), (6, 6, 4, 6, 6, 4, 4), (5, 5, 6, 6, 5, 6, 5), (6, 6, 6, 6, 6, 6, 6))),
    (5, ((4, 1, 0, 0, 3), (2, 1, 2, 2, 2), (2, 1, 2, 2, 2), (4, 1, 3, 0, 3), (4, 1, 4, 0, 3))),
    (7, ((0, 4, 4, 0, 4, 0, 0), (2, 2, 3, 1, 1, 3, 2), (3, 2, 3, 6, 2, 3, 2), (3, 2, 3, 6, 3, 3, 5), (0, 4, 4, 4, 4, 4, 4), (5, 5, 3, 6, 5, 3, 5), (6, 5, 3, 6, 6, 3, 5))),
    (6, ((0, 2, 2, 0, 0, 0), (1, 4, 1, 4, 5, 1), (0, 0, 2, 2, 2, 2), (3, 4, 3, 4, 5, 3), (4, 4, 4, 4, 5, 3), (5, 4, 5, 4, 5, 3))),
    (6, ((1, 3, 4, 0, 5, 2), (2, 3, 4, 5, 0, 1), (2, 3, 4, 5, 0, 1), (1, 4, 3, 5, 0, 2), (1, 4, 3, 5, 0, 2), (1, 3, 4, 0, 5, 2))),
    (7, ((1, 5, 6, 3, 0, 2, 4), (2, 4, 3, 1, 6, 5, 0), (3, 2, 0, 6, 4, 1, 5), (4, 6, 2, 5, 1, 0, 3), (5, 0, 1, 2, 3, 4, 6), (0, 3, 5, 4, 2, 6, 1), (6, 1, 4, 0, 5, 3, 2))),
    (5, ((2, 1, 3, 0, 4), (2, 1, 3, 0, 4), (2, 4, 3, 0, 1), (2, 4, 3, 0, 1), (2, 4, 3, 0, 1))),
    (7, ((5, 6, 3, 2, 4, 0, 1), (3, 2, 6, 4, 0, 1, 5), (6, 1, 5, 3, 4, 2, 0), (0, 1, 4, 5, 2, 3, 6), (2, 3, 0, 1, 5, 4, 6), (0, 1, 2, 3, 6, 5, 4), (3, 5, 1, 4, 0, 6, 2))),
    (7, ((0, 2, 5, 6, 3, 1, 4), (2, 1, 3, 0, 6, 4, 5), (5, 3, 2, 4, 1, 6, 0), (6, 0, 4, 3, 5, 2, 1), (3, 6, 1, 5, 4, 0, 2), (1, 4, 6, 2, 0, 5, 3), (4, 5, 0, 1, 2, 3, 6))),
    (7, ((2, 6, 5, 4, 1, 0, 3), (2, 6, 3, 5, 1, 0, 4), (2, 3, 5, 6, 1, 0, 4), (4, 0, 1, 3, 5, 6, 2), (2, 6, 5, 0, 1, 3, 4), (2, 6, 5, 1, 3, 0, 4), (3, 6, 5, 2, 1, 0, 4))),
    (5, ((0, 2, 3, 1, 4), (0, 2, 3, 1, 4), (4, 2, 3, 1, 0), (0, 2, 3, 1, 4), (0, 2, 3, 1, 4))),
    (5, ((0, 1, 2, 4, 3), (0, 1, 3, 2, 4), (1, 0, 2, 3, 4), (1, 0, 2, 3, 4), (1, 0, 2, 3, 4))),
    (6, ((2, 3, 4, 5, 0, 1), (2, 3, 0, 5, 4, 1), (2, 3, 4, 5, 0, 1), (4, 3, 2, 5, 0, 1), (2, 3, 4, 5, 0, 1), (0, 3, 4, 5, 2, 1))),
    (8, ((5, 3, 1, 2, 7, 0, 6, 4), (2, 5, 4, 3, 0, 1, 7, 6), (4, 7, 5, 1, 6, 2, 0, 3), (6, 4, 0, 5, 1, 3, 2, 7), (0, 2, 7, 6, 5, 4, 3, 1), (7, 6, 2, 4, 3, 5, 1, 0), (1, 0, 3, 7, 4, 6, 5, 2), (3, 1, 6, 0, 2, 7, 4, 5))),
    (7, ((1, 1, 0, 1, 2, 2, 1), (2, 5, 1, 5, 2, 5, 5), (1, 5, 4, 4, 3, 0, 3), (0, 1, 4, 6, 2, 5, 3), (3, 3, 3, 2, 2, 3, 3), (0, 2, 5, 0, 2, 0, 0), (0, 1, 3, 3, 3, 5, 3))),
    (6, ((3, 3, 3, 0, 0, 3), (2, 5, 5, 5, 2, 2), (3, 5, 4, 0, 2, 1), (0, 5, 0, 0, 0, 1), (0, 2, 2, 0, 2, 2), (2, 2, 1, 1, 2, 1))),
    (6, ((1, 4, 4, 4, 3, 2), (0, 2, 4, 2, 4, 5), (0, 3, 2, 2, 2, 5), (5, 2, 2, 2, 1, 0), (5, 1, 1, 1, 2, 0), (2, 4, 4, 4, 3, 1))),
    (7, ((1, 5, 4, 1, 3, 6, 2), (3, 0, 5, 6, 2, 0, 4), (6, 4, 0, 5, 0, 1, 3), (4, 0, 6, 0, 5, 2, 1), (2, 6, 1, 0, 2, 3, 5), (1, 2, 3, 4, 6, 1, 0), (5, 3, 0, 2, 1, 4, 5))),
    (7, ((1, 6, 3, 4, 5, 3, 2), (2, 1, 2, 1, 1, 5, 1), (6, 2, 2, 2, 5, 6, 4), (5, 1, 2, 3, 3, 5, 1), (3, 1, 6, 3, 4, 4, 6), (4, 5, 4, 5, 4, 5, 5), (1, 1, 5, 1, 6, 5, 6))),
    (6, ((1, 4, 1, 4, 3, 2), (2, 5, 4, 1, 4, 1), (3, 4, 3, 2, 1, 2), (4, 1, 2, 3, 4, 5), (3, 4, 1, 4, 3, 2), (4, 1, 2, 5, 2, 3))),
    (7, ((1, 4, 1, 5, 3, 6, 2), (2, 0, 5, 6, 0, 3, 4), (6, 0, 2, 4, 5, 1, 3), (4, 5, 6, 3, 2, 0, 1), (1, 6, 3, 0, 2, 2, 5), (3, 2, 4, 1, 6, 0, 0), (5, 3, 0, 2, 1, 4, 0))),
    (6, ((1, 0, 0, 4, 2, 0), (3, 2, 1, 1, 5, 2), (3, 2, 2, 1, 5, 1), (3, 3, 2, 2, 5, 1), (2, 1, 4, 4, 1, 0), (3, 2, 2, 1, 5, 2))),
    (7, ((0, 0, 6, 4, 0, 6, 0), (2, 2, 2, 2, 2, 2, 2), (3, 3, 3, 3, 3, 3, 3), (5, 5, 5, 5, 5, 5, 5), (4, 4, 0, 6, 4, 0, 4), (1, 1, 1, 1, 1, 1, 1), (6, 6, 4, 0, 6, 4, 6))),
    (8, ((1, 5, 3, 7, 2, 4, 6, 0), (2, 0, 7, 3, 1, 6, 4, 5), (4, 3, 5, 0, 6, 1, 2, 7), (5, 1, 4, 6, 0, 3, 7, 2), (3, 4, 1, 2, 7, 5, 0, 6), (6, 7, 0, 5, 4, 2, 1, 3), (0, 2, 6, 4, 5, 7, 3, 1), (7, 6, 2, 1, 3, 0, 5, 4))),
    (8, ((1, 2, 3, 6, 3, 6, 1, 2), (2, 5, 6, 5, 6, 3, 2, 3), (7, 4, 5, 0, 5, 0, 7, 4), (6, 7, 2, 7, 2, 1, 6, 1), (3, 6, 1, 2, 1, 2, 3, 6), (4, 3, 0, 3, 0, 5, 4, 7), (5, 0, 7, 4, 7, 4, 5, 0), (0, 1, 4, 1, 4, 7, 0, 5))),
    (8, ((2, 3, 1, 6, 0, 4, 5, 7), (7, 0, 6, 2, 4, 3, 1, 5), (3, 1, 5, 7, 2, 0, 4, 6), (1, 7, 3, 4, 6, 5, 0, 2), (5, 2, 4, 0, 7, 1, 6, 3), (0, 5, 7, 1, 3, 6, 2, 4), (4, 6, 2, 5, 1, 7, 3, 0), (6, 4, 0, 3, 5, 2, 7, 1))),
    (8, ((1, 5, 6, 3, 7, 2, 4, 0), (2, 4, 3, 6, 0, 1, 5, 7), (3, 7, 2, 1, 5, 6, 0, 4), (5, 1, 0, 7, 3, 4, 2, 6), (4, 2, 7, 0, 6, 5, 1, 3), (7, 3, 4, 5, 1, 0, 6, 2), (0, 6, 5, 4, 2, 7, 3, 1), (6, 0, 1, 2, 4, 3, 7, 5))),
    (7, ((1, 6, 2, 0, 5, 3, 4), (2, 4, 5, 3, 0, 6, 1), (0, 2, 3, 4, 6, 1, 5), (5, 1, 0, 6, 3, 4, 2), (4, 3, 1, 5, 2, 0, 6), (6, 0, 4, 2, 1, 5, 3), (3, 5, 6, 1, 4, 2, 0))),
    (5, ((3, 2, 3, 3, 3), (1, 4, 1, 1, 4), (2, 3, 2, 2, 0), (0, 0, 0, 0, 2), (4, 1, 4, 4, 1))),
    (5, ((2, 1, 3, 1, 2), (3, 1, 3, 1, 3), (4, 0, 0, 0, 4), (2, 0, 0, 0, 2), (4, 0, 0, 0, 4))),
    (5, ((0, 0, 3, 0, 0), (2, 1, 1, 2, 2), (0, 4, 4, 0, 4), (2, 2, 2, 2, 2), (1, 1, 1, 1, 1))),
    (6, ((1, 3, 5, 1, 2, 2), (2, 4, 1, 0, 5, 1), (3, 2, 4, 2, 3, 0), (5, 0, 3, 4, 2, 3), (5, 1, 2, 3, 5, 5), (1, 5, 0, 5, 1, 4))),
    (6, ((1, 2, 3, 1, 3, 2), (5, 5, 0, 4, 0, 4), (0, 0, 4, 5, 4, 5), (4, 4, 5, 0, 5, 0), (3, 1, 2, 3, 2, 1), (2, 3, 1, 2, 1, 3))),
    (6, ((1, 2, 3, 2, 2, 4), (5, 1, 2, 3, 3, 0), (3, 0, 4, 0, 0, 1), (2, 3, 0, 1, 1, 5), (0, 4, 5, 4, 4, 2), (4, 5, 1, 5, 5, 3))),
    (6, ((1, 2, 3, 5, 1, 1), (3, 4, 2, 0, 1, 5), (5, 1, 4, 3, 2, 0), (1, 0, 2, 4, 3, 5), (3, 2, 1, 5, 2, 3), (2, 1, 0, 3, 5, 4))),
    (5, ((1, 2, 4, 0, 3), (0, 3, 4, 1, 3), (3, 2, 2, 0, 1), (4, 1, 4, 3, 0), (2, 0, 2, 2, 4))),
    (8, ((1, 5, 5, 1, 1, 1, 5, 5), (2, 0, 0, 2, 2, 2, 0, 0), (3, 1, 1, 3, 3, 3, 1, 1), (4, 2, 2, 4, 4, 4, 2, 2), (7, 3, 3, 7, 7, 7, 3, 3), (0, 6, 6, 0, 0, 0, 6, 6), (5, 7, 7, 5, 5, 5, 7, 7), (6, 4, 4, 6, 6, 6, 4, 4))),
    (8, ((2, 4, 0, 2, 5, 0, 5, 4), (0, 3, 0, 3, 0, 0, 3, 3), (0, 3, 0, 3, 0, 0, 3, 3), (1, 3, 6, 1, 7, 6, 7, 3), (1, 3, 0, 1, 7, 0, 7, 3), (4, 4, 6, 4, 6, 6, 6, 4), (2, 4, 6, 2, 5, 6, 5, 4), (4, 4, 6, 4, 6, 6, 6, 4))),
    (8, ((2, 2, 6, 2, 2, 6, 6, 6), (3, 2, 3, 3, 2, 2, 3, 2), (3, 7, 4, 1, 2, 6, 0, 5), (3, 2, 0, 3, 2, 6, 0, 6), (2, 2, 2, 2, 2, 2, 2, 2), (2, 7, 7, 7, 2, 2, 2, 7), (2, 7, 5, 7, 2, 6, 6, 5), (3, 7, 1, 1, 2, 2, 3, 7))),
    (5, ((1, 4, 1, 4, 4), (2, 0, 2, 2, 0), (3, 3, 2, 2, 0), (1, 0, 1, 2, 0), (3, 3, 1, 4, 4))),
    (6, ((1, 5, 3, 2, 0, 4), (2, 1, 0, 3, 4, 5), (3, 2, 4, 0, 5, 1), (2, 1, 0, 5, 4, 3), (2, 4, 0, 3, 1, 5), (4, 0, 1, 3, 2, 5))),
    (8, ((1, 2, 3, 4, 6, 7, 5, 0), (7, 0, 1, 2, 3, 6, 4, 5), (7, 0, 1, 2, 3, 6, 4, 5), (1, 2, 3, 4, 6, 7, 5, 0), (1, 2, 3, 4, 6, 7, 5, 0), (7, 0, 1, 2, 3, 6, 4, 5), (7, 0, 1, 2, 3, 6, 4, 5), (1, 2, 3, 4, 6, 7, 5, 0))),
    (8, ((2, 4, 7, 5, 0, 6, 1, 3), (0, 5, 2, 1, 7, 4, 3, 6), (3, 1, 4, 6, 5, 0, 2, 7), (7, 2, 3, 0, 4, 1, 6, 5), (1, 3, 0, 7, 6, 2, 5, 4), (5, 7, 6, 4, 1, 3, 0, 2), (4, 6, 1, 3, 2, 5, 7, 0), (6, 0, 5, 2, 3, 7, 4, 1))),
    (8, ((1, 2, 5, 7, 3, 0, 4, 6), (2, 3, 4, 6, 7, 5, 1, 0), (3, 7, 6, 2, 1, 4, 0, 5), (7, 3, 0, 6, 2, 5, 1, 4), (3, 7, 6, 2, 1, 4, 0, 5), (2, 3, 4, 6, 7, 5, 1, 0), (7, 3, 0, 6, 2, 5, 1, 4), (1, 2, 5, 7, 3, 0, 4, 6))),
    (7, ((1, 2, 5, 6, 4, 3, 0), (3, 0, 6, 4, 2, 5, 1), (0, 4, 3, 5, 6, 1, 2), (5, 1, 4, 2, 0, 6, 3), (2, 6, 1, 3, 5, 0, 4), (6, 3, 2, 0, 1, 4, 5), (4, 5, 0, 1, 3, 2, 6))),
    (5, ((1, 0, 3, 4, 2), (2, 3, 2, 1, 0), (4, 4, 2, 4, 2), (0, 1, 0, 3, 2), (3, 3, 1, 0, 4))),
    (7, ((0, 2, 5, 0, 6, 2, 4), (3, 3, 3, 3, 3, 3, 3), (4, 6, 2, 2, 0, 6, 5), (1, 1, 1, 1, 1, 1, 1), (5, 0, 6, 4, 4, 0, 2), (6, 5, 4, 5, 2, 5, 0), (2, 4, 0, 6, 5, 4, 6))),
    (6, ((1, 2, 3, 5, 2, 4), (0, 1, 2, 3, 4, 5), (5, 3, 1, 4, 0, 3), (4, 4, 0, 1, 5, 2), (3, 5, 5, 2, 1, 0), (2, 0, 4, 0, 3, 1))),
    (6, ((1, 0, 5, 4, 3, 2), (2, 1, 3, 4, 5, 0), (3, 2, 1, 0, 5, 4), (5, 3, 4, 1, 2, 0), (2, 4, 0, 5, 1, 3), (4, 5, 3, 2, 0, 1))),
    (8, ((1, 0, 3, 2, 4, 5, 6, 7), (2, 5, 3, 4, 0, 1, 6, 7), (4, 1, 3, 2, 0, 5, 6, 7), (1, 0, 3, 2, 7, 5, 6, 4), (6, 1, 3, 2, 4, 5, 0, 7), (4, 5, 0, 2, 3, 1, 6, 7), (0, 1, 3, 2, 4, 5, 6, 7), (1, 0, 3, 2, 4, 5, 6, 7))),
)
# END GENERATED PUBLIC MAGMA CATALOG

VAR = "var"
OP = "op"
META = "meta"


class EquationSyntaxError(ValueError):
    """Raised when a public equation is outside the supported grammar."""


def normalize_operator(text):
    """Normalize the dataset's alternate display operator to Lean's ``◇``."""
    if not isinstance(text, str):
        raise EquationSyntaxError("equation must be a string")
    return text.replace("*", "◇")


def _tokenize(text):
    text = normalize_operator(text)
    tokens = []
    for index, char in enumerate(text):
        if char.isspace():
            continue
        if char in "()=◇":
            tokens.append(char)
            continue
        if "a" <= char <= "z":
            tokens.append(char)
            continue
        raise EquationSyntaxError(
            "unsupported character {!r} at offset {}".format(char, index)
        )
    return tokens


class _EquationParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        if self.position >= len(self.tokens):
            return None
        return self.tokens[self.position]

    def take(self, expected=None):
        token = self.peek()
        if token is None:
            raise EquationSyntaxError("unexpected end of equation")
        if expected is not None and token != expected:
            raise EquationSyntaxError(
                "expected {!r}, found {!r}".format(expected, token)
            )
        self.position += 1
        return token

    def parse_atom(self):
        token = self.peek()
        if token == "(":
            self.take("(")
            term = self.parse_term()
            self.take(")")
            return term
        if token is not None and len(token) == 1 and "a" <= token <= "z":
            self.take()
            return (VAR, token)
        raise EquationSyntaxError("expected a variable or parenthesized term")

    def parse_term(self):
        # Unparenthesized chains are interpreted left-associatively, matching
        # Lean's infixl declaration.  The official dataset is mostly explicit.
        term = self.parse_atom()
        while self.peek() == "◇":
            self.take("◇")
            term = (OP, term, self.parse_atom())
        return term


def parse_equation(text):
    """Parse ``lhs = rhs`` into immutable AST tuples and binder order."""
    parser = _EquationParser(_tokenize(text))
    lhs = parser.parse_term()
    parser.take("=")
    rhs = parser.parse_term()
    if parser.peek() is not None:
        raise EquationSyntaxError("unexpected trailing token {!r}".format(parser.peek()))
    return lhs, rhs, variables_in_order(lhs, rhs)


def variables_in_order(*terms):
    seen = set()
    result = []

    def visit(term):
        if term[0] == VAR:
            if term[1] not in seen:
                seen.add(term[1])
                result.append(term[1])
            return
        visit(term[1])
        visit(term[2])

    for term in terms:
        visit(term)
    return result


def variables_set(term):
    return set(variables_in_order(term))


def render_term(term):
    if term[0] == VAR:
        return term[1]
    return "({} ◇ {})".format(render_term(term[1]), render_term(term[2]))


def _alpha_normalize_pair(lhs, rhs):
    names = {}

    def rename(term):
        if term[0] == VAR:
            old = term[1]
            if old not in names:
                names[old] = "v{}".format(len(names))
            return (VAR, names[old])
        return (OP, rename(term[1]), rename(term[2]))

    return rename(lhs), rename(rhs)


def canonical_equation(text):
    """Return an alpha-normalized, side-symmetry-normalized equation AST."""
    lhs, rhs, _ = parse_equation(text)
    forward = _alpha_normalize_pair(lhs, rhs)
    reverse = _alpha_normalize_pair(rhs, lhs)
    return min(forward, reverse)


def canonical_equation_text(text):
    lhs, rhs = canonical_equation(text)
    return "{} = {}".format(render_term(lhs), render_term(rhs))


def term_size(term):
    if term[0] == VAR:
        return 1
    return 1 + term_size(term[1]) + term_size(term[2])


def iter_subterms(term):
    yield term
    if term[0] == OP:
        yield from iter_subterms(term[1])
        yield from iter_subterms(term[2])


def evaluate_term(term, environment, table):
    if term[0] == VAR:
        return environment[term[1]]
    left = evaluate_term(term[1], environment, table)
    right = evaluate_term(term[2], environment, table)
    return table[left][right]


def validate_table(
    table, minimum=2, maximum=MAX_INTERNAL_COUNTERMODEL_CARRIER
):
    """Return the carrier size for a valid finite table, otherwise ``None``."""
    if not isinstance(table, list):
        return None
    n = len(table)
    if n < minimum or n > maximum:
        return None
    for row in table:
        if not isinstance(row, list) or len(row) != n:
            return None
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                return None
            if value < 0 or value >= n:
                return None
    return n


def equation_holds(parsed_equation, n, table):
    lhs, rhs, variables = parsed_equation
    for values in product(range(n), repeat=len(variables)):
        environment = dict(zip(variables, values))
        if evaluate_term(lhs, environment, table) != evaluate_term(
            rhs, environment, table
        ):
            return False
    return True


def verify_counterexample(eq1_text, eq2_text, table):
    n = validate_table(table)
    if n is None:
        return False, False
    eq1 = parse_equation(eq1_text)
    eq2 = parse_equation(eq2_text)
    return equation_holds(eq1, n, table), equation_holds(eq2, n, table)


def _decode_table(n, encoded):
    values = []
    for _ in range(n * n):
        values.append(encoded % n)
        encoded //= n
    return [values[row * n : (row + 1) * n] for row in range(n)]


def search_exhaustive_counterexample(eq1_text, eq2_text, max_n=3):
    """Completely enumerate every operation table on Fin 2 through Fin 3.

    The final boolean records that the fixed finite search completed.
    """
    eq1 = parse_equation(eq1_text)
    eq2 = parse_equation(eq2_text)
    for n in range(2, max_n + 1):
        total = n ** (n * n)
        for encoded in range(total):
            table = _decode_table(n, encoded)
            if equation_holds(eq1, n, table) and not equation_holds(eq2, n, table):
                return n, table, True
    return None, None, True


def structured_tables(n):
    """Yield a fixed, duplicate-free catalog of structured Fin-n magmas."""
    tables = []
    seen = set()

    def add(table):
        key = tuple(value for row in table for value in row)
        if key not in seen:
            seen.add(key)
            tables.append(table)

    # Constants, projections, semilattices, and small arithmetic families.
    for constant in range(n):
        add([[constant for _ in range(n)] for _ in range(n)])
    add([[left for _ in range(n)] for left in range(n)])
    add([[right for right in range(n)] for _ in range(n)])
    add([[min(left, right) for right in range(n)] for left in range(n)])
    add([[max(left, right) for right in range(n)] for left in range(n)])
    add([[(left + right) % n for right in range(n)] for left in range(n)])
    add([[(left - right) % n for right in range(n)] for left in range(n)])
    add([[(right - left) % n for right in range(n)] for left in range(n)])
    add([[(left * right) % n for right in range(n)] for left in range(n)])
    add([[(left ^ right) % n for right in range(n)] for left in range(n)])
    add([[(left & right) % n for right in range(n)] for left in range(n)])
    add([[(left | right) % n for right in range(n)] for left in range(n)])

    # Exhaust the complete affine family a*x + b*y + c on each fixed carrier.
    # This remains a small deterministic catalog (at most 336 nonconstant
    # coefficient triples on Fin 7) and avoids the blind spot from truncating
    # coefficients or constants on the larger carriers.
    coefficients = range(n)
    constants = range(n)
    for left_coefficient in coefficients:
        for right_coefficient in coefficients:
            if left_coefficient == 0 and right_coefficient == 0:
                continue
            for constant in constants:
                add(
                    [
                        [
                            (
                                left_coefficient * left
                                + right_coefficient * right
                                + constant
                            )
                            % n
                            for right in range(n)
                        ]
                        for left in range(n)
                    ]
                )

    # Idempotent, absorbing, shift, and selector-shaped operations.
    add(
        [
            [left if left == right else 0 for right in range(n)]
            for left in range(n)
        ]
    )
    add(
        [
            [left if left == right else n - 1 for right in range(n)]
            for left in range(n)
        ]
    )
    add(
        [
            [left if left != 0 else right for right in range(n)]
            for left in range(n)
        ]
    )
    add(
        [
            [right if right != 0 else left for right in range(n)]
            for left in range(n)
        ]
    )
    add([[n - 1 - left for _ in range(n)] for left in range(n)])
    add([[n - 1 - right for right in range(n)] for _ in range(n)])
    for shift in range(1, min(n, 4)):
        add([[(left + shift) % n for _ in range(n)] for left in range(n)])
        add([[(right + shift) % n for right in range(n)] for _ in range(n)])

    # Rectangular bands for composite carrier sizes.
    for divisor in range(2, n):
        if n % divisor:
            continue
        width = n // divisor
        add(
            [
                [(left // width) * width + (right % width) for right in range(n)]
                for left in range(n)
            ]
        )

    for table in tables:
        yield table


def search_structured_counterexample(
    eq1_text, eq2_text, sizes=(4, 5, 6, 7)
):
    eq1 = parse_equation(eq1_text)
    eq2 = parse_equation(eq2_text)
    for n in sizes:
        for table in structured_tables(n):
            if equation_holds(eq1, n, table) and not equation_holds(eq2, n, table):
                return n, table, True
    return None, None, True


def fixed_generated_countermodels():
    """Yield fresh copies of provenance-recorded deterministic tables."""
    for n, rows in FIXED_GENERATED_COUNTERMODEL_TABLES:
        yield n, [list(row) for row in rows]


def search_fixed_generated_counterexample(eq1_text, eq2_text):
    eq1 = parse_equation(eq1_text)
    eq2 = parse_equation(eq2_text)
    for n, table in fixed_generated_countermodels():
        if equation_holds(eq1, n, table) and not equation_holds(eq2, n, table):
            return n, table, True
    return None, None, True


def public_magma_catalog():
    """Yield fresh ID-free tables from the pinned public global corpus."""
    for n, rows in PUBLIC_MAGMA_CATALOG:
        yield n, [list(row) for row in rows]


def search_public_magma_catalog_counterexample(eq1_text, eq2_text):
    """Test the complete generated ID-free public magma catalog."""
    eq1 = parse_equation(eq1_text)
    eq2 = parse_equation(eq2_text)
    for n, table in public_magma_catalog():
        if equation_holds(eq1, n, table) and not equation_holds(eq2, n, table):
            return n, table, True
    return None, None, True


def large_public_countermodels():
    """Yield fresh ID-free Fin 9 and Fin 13 public coverage-plan models."""
    for n, rows in LARGE_PUBLIC_COUNTERMODEL_TABLES:
        yield n, [list(row) for row in rows]


def search_large_public_counterexample(eq1_text, eq2_text):
    """Test larger public models only when a bounded structural proof fits."""
    eq1 = parse_equation(eq1_text)
    eq2 = parse_equation(eq2_text)
    for n, table in large_public_countermodels():
        if n ** len(eq1[2]) > MAX_STRUCTURAL_COUNTERMODEL_CASES:
            continue
        if equation_holds(eq1, n, table) and not equation_holds(eq2, n, table):
            return n, table, True
    return None, None, True


def _dual_number_pair(value):
    """Decode one element of F_3[eps]/(eps^2) as (constant, eps)."""
    return divmod(value, 3)


def _dual_number_encode(constant, epsilon):
    return (constant % 3) * 3 + (epsilon % 3)


def _dual_number_add(left, right):
    left_constant, left_epsilon = _dual_number_pair(left)
    right_constant, right_epsilon = _dual_number_pair(right)
    return _dual_number_encode(
        left_constant + right_constant,
        left_epsilon + right_epsilon,
    )


def _dual_number_mul(left, right):
    left_constant, left_epsilon = _dual_number_pair(left)
    right_constant, right_epsilon = _dual_number_pair(right)
    return _dual_number_encode(
        left_constant * right_constant,
        left_constant * right_epsilon + left_epsilon * right_constant,
    )


def _dual_affine_scale(coefficient, affine_form):
    variable_coefficients, constant = affine_form
    scaled = {}
    for variable, value in variable_coefficients.items():
        product = _dual_number_mul(coefficient, value)
        if product != 0:
            scaled[variable] = product
    return scaled, _dual_number_mul(coefficient, constant)


def _dual_affine_add(left, right):
    left_coefficients, left_constant = left
    right_coefficients, right_constant = right
    zero = _dual_number_encode(0, 0)
    coefficients = {}
    for variable in sorted(set(left_coefficients) | set(right_coefficients)):
        value = _dual_number_add(
            left_coefficients.get(variable, zero),
            right_coefficients.get(variable, zero),
        )
        if value != zero:
            coefficients[variable] = value
    return coefficients, _dual_number_add(left_constant, right_constant)


def _dual_affine_term_form(term, left_coefficient, right_coefficient, constant):
    zero = _dual_number_encode(0, 0)
    one = _dual_number_encode(1, 0)
    if term[0] == VAR:
        return {term[1]: one}, zero
    left = _dual_affine_term_form(
        term[1], left_coefficient, right_coefficient, constant
    )
    right = _dual_affine_term_form(
        term[2], left_coefficient, right_coefficient, constant
    )
    combined = _dual_affine_add(
        _dual_affine_scale(left_coefficient, left),
        _dual_affine_scale(right_coefficient, right),
    )
    return combined[0], _dual_number_add(combined[1], constant)


def _dual_affine_equation_holds_symbolically(
    parsed_equation, left_coefficient, right_coefficient, constant
):
    lhs, rhs, _ = parsed_equation
    return _dual_affine_term_form(
        lhs, left_coefficient, right_coefficient, constant
    ) == _dual_affine_term_form(
        rhs, left_coefficient, right_coefficient, constant
    )


def _dual_affine_table(left_coefficient, right_coefficient, constant):
    return [
        [
            _dual_number_add(
                _dual_number_add(
                    _dual_number_mul(left_coefficient, left),
                    _dual_number_mul(right_coefficient, right),
                ),
                constant,
            )
            for right in range(9)
        ]
        for left in range(9)
    ]


def search_dual_number_affine_counterexample(eq1_text, eq2_text):
    """Search the full affine family over F_3[eps]/(eps^2), fail closed.

    Symbolic affine identities make the 9^3 coefficient scan cheap.  Any hit is
    then rebuilt as an explicit Fin-9 magma and exhaustively revalidated before
    it can reach the structural Lean certificate generator.
    """
    hypothesis = parse_equation(eq1_text)
    goal = parse_equation(eq2_text)
    for left_coefficient in range(9):
        for right_coefficient in range(9):
            for constant in range(9):
                if not _dual_affine_equation_holds_symbolically(
                    hypothesis,
                    left_coefficient,
                    right_coefficient,
                    constant,
                ):
                    continue
                if _dual_affine_equation_holds_symbolically(
                    goal,
                    left_coefficient,
                    right_coefficient,
                    constant,
                ):
                    continue
                table = _dual_affine_table(
                    left_coefficient, right_coefficient, constant
                )
                if equation_holds(hypothesis, 9, table) and not equation_holds(
                    goal, 9, table
                ):
                    return 9, table, True
    return None, None, True



@dataclass(frozen=True)
class _PGAPAffine:
    constant: int
    coefficients: tuple

    @staticmethod
    def variable(index, count):
        coefficients = [0] * count
        coefficients[index] = 1
        return _PGAPAffine(0, tuple(coefficients))

    def scale(self, factor):
        return _PGAPAffine(
            self.constant * factor,
            tuple(factor * value for value in self.coefficients),
        )

    def add(self, other):
        return _PGAPAffine(
            self.constant + other.constant,
            tuple(
                left + right
                for left, right in zip(self.coefficients, other.coefficients)
            ),
        )

    def shift(self, constant):
        return _PGAPAffine(self.constant + constant, self.coefficients)


@dataclass(frozen=True)
class _PGAPConstraint:
    """Halfspace ``sum(coefficients[i] * x[i]) <= rhs``."""

    coefficients: tuple
    rhs: int


@dataclass(frozen=True)
class _PGAPPiece:
    constraints: tuple
    value: _PGAPAffine


@dataclass(frozen=True)
class _PGAPModel:
    """Polyhedral Guarded Action Program over the infinite carrier Int.

    The sign of the already-evaluated left operand selects one of two affine
    payload programs.  Unlike a finite Cayley table or one global affine law,
    an intermediate term may dynamically cross the guard and change the action
    applied to its sibling.  The six coefficients are synthesized from a tiny
    bounded grammar; no problem IDs, answers, or equivalence classes are used.
    """

    positive_left: int
    positive_right: int
    positive_constant: int
    negative_left: int
    negative_right: int
    negative_constant: int

    def apply(self, left, right):
        if left >= 0:
            return (
                self.positive_left * left
                + self.positive_right * right
                + self.positive_constant
            )
        return (
            self.negative_left * left
            + self.negative_right * right
            + self.negative_constant
        )

    def affine_value(self, positive, left, right):
        if positive:
            left_coefficient = self.positive_left
            right_coefficient = self.positive_right
            constant = self.positive_constant
        else:
            left_coefficient = self.negative_left
            right_coefficient = self.negative_right
            constant = self.negative_constant
        return left.scale(left_coefficient).add(
            right.scale(right_coefficient)
        ).shift(constant)


def _pgap_evaluate_term(term, environment, model):
    if term[0] == VAR:
        return environment[term[1]]
    return model.apply(
        _pgap_evaluate_term(term[1], environment, model),
        _pgap_evaluate_term(term[2], environment, model),
    )


def _pgap_positive_constraint(value):
    # value >= 0  iff  -linear(value) <= constant(value).
    return _PGAPConstraint(
        tuple(-coefficient for coefficient in value.coefficients),
        value.constant,
    )


def _pgap_negative_constraint(value):
    # On Int, value < 0 iff value <= -1.
    return _PGAPConstraint(value.coefficients, -1 - value.constant)


def _pgap_deduplicate_constraints(constraints):
    tightest = {}
    variable_count = 0
    for constraint in constraints:
        variable_count = len(constraint.coefficients)
        if not any(constraint.coefficients):
            if constraint.rhs < 0:
                return (_PGAPConstraint((0,) * variable_count, -1),)
            continue
        previous = tightest.get(constraint.coefficients)
        if previous is None or constraint.rhs < previous:
            tightest[constraint.coefficients] = constraint.rhs
    return tuple(
        _PGAPConstraint(coefficients, rhs)
        for coefficients, rhs in sorted(tightest.items())
    )


def _pgap_expand_term(term, variables, model):
    variable_index = {
        variable: index for index, variable in enumerate(variables)
    }
    variable_count = len(variables)

    def expand(node):
        if node[0] == VAR:
            return (
                _PGAPPiece(
                    (),
                    _PGAPAffine.variable(
                        variable_index[node[1]], variable_count
                    ),
                ),
            )
        left_pieces = expand(node[1])
        right_pieces = expand(node[2])
        pieces = []
        for left_piece in left_pieces:
            for right_piece in right_pieces:
                base = left_piece.constraints + right_piece.constraints
                for positive in (True, False):
                    guard = (
                        _pgap_positive_constraint(left_piece.value)
                        if positive
                        else _pgap_negative_constraint(left_piece.value)
                    )
                    pieces.append(
                        _PGAPPiece(
                            _pgap_deduplicate_constraints(base + (guard,)),
                            model.affine_value(
                                positive,
                                left_piece.value,
                                right_piece.value,
                            ),
                        )
                    )
        return tuple(dict.fromkeys(pieces))

    return expand(term)


def _pgap_rational_region_feasible(constraints, variable_count):
    """Exact Fourier--Motzkin feasibility over Q.

    Every integer point is a rational point.  Consequently, discarding only a
    rationally infeasible branch is sound for universal identities on Int.  A
    feasible relaxation whose two affine outputs differ rejects the candidate,
    so this checker can have false negatives but never certify a false model.
    """
    rows = []
    for constraint in constraints:
        coefficients = [Fraction(value) for value in constraint.coefficients]
        rhs = Fraction(constraint.rhs)
        if not any(coefficients):
            if rhs < 0:
                return False
            continue
        rows.append((coefficients, rhs))

    for variable in range(variable_count):
        positive_rows = []
        negative_rows = []
        zero_rows = []
        for coefficients, rhs in rows:
            coefficient = coefficients[variable]
            if coefficient > 0:
                positive_rows.append((coefficients, rhs))
            elif coefficient < 0:
                negative_rows.append((coefficients, rhs))
            else:
                zero_rows.append((coefficients, rhs))

        next_rows = []
        for coefficients, rhs in zero_rows:
            copied = list(coefficients)
            copied[variable] = Fraction(0)
            next_rows.append((copied, rhs))

        if positive_rows and negative_rows:
            for upper_coefficients, upper_rhs in positive_rows:
                upper = upper_coefficients[variable]
                for lower_coefficients, lower_rhs in negative_rows:
                    lower = lower_coefficients[variable]
                    combined = [
                        (-lower) * first + upper * second
                        for first, second in zip(
                            upper_coefficients, lower_coefficients
                        )
                    ]
                    combined[variable] = Fraction(0)
                    combined_rhs = (
                        (-lower) * upper_rhs + upper * lower_rhs
                    )
                    if not any(combined):
                        if combined_rhs < 0:
                            return False
                        continue
                    next_rows.append((combined, combined_rhs))

        tightest = {}
        for coefficients, rhs in next_rows:
            key = tuple(coefficients)
            previous = tightest.get(key)
            if previous is None or rhs < previous:
                tightest[key] = rhs
        rows = [
            (list(coefficients), rhs)
            for coefficients, rhs in tightest.items()
        ]
    return True


def _pgap_equation_holds_symbolically(parsed_equation, model):
    lhs, rhs, variables = parsed_equation
    lhs_pieces = _pgap_expand_term(lhs, variables, model)
    rhs_pieces = _pgap_expand_term(rhs, variables, model)
    for lhs_piece in lhs_pieces:
        for rhs_piece in rhs_pieces:
            constraints = _pgap_deduplicate_constraints(
                lhs_piece.constraints + rhs_piece.constraints
            )
            if not _pgap_rational_region_feasible(
                constraints, len(variables)
            ):
                continue
            if lhs_piece.value != rhs_piece.value:
                return False
    return True


def _pgap_counterexample_witness(parsed_equation, model, radius=3):
    lhs, rhs, variables = parsed_equation
    domain = tuple(
        sorted(range(-radius, radius + 1), key=lambda value: (abs(value), value))
    )
    for values in product(domain, repeat=len(variables)):
        environment = dict(zip(variables, values))
        lhs_value = _pgap_evaluate_term(lhs, environment, model)
        rhs_value = _pgap_evaluate_term(rhs, environment, model)
        if lhs_value != rhs_value:
            return values, lhs_value, rhs_value
    return None


def search_polyhedral_guarded_action_counterexample(
    eq1_text,
    eq2_text,
    coefficients=(-1, 0, 1),
    constants=(-1, 0, 1),
    sample_radius=1,
    witness_radius=3,
):
    """Synthesize an infinite, dynamically guarded affine countermodel.

    A cheap integer sample rejects most programs.  Any survivor must pass the
    exact polyhedral universal checker above; the goal must then fail at a
    concrete deterministic integer assignment.  The returned tuple is ready
    for the Lean certificate compiler and contains no dataset identifiers.
    """
    hypothesis = parse_equation(eq1_text)
    goal = parse_equation(eq2_text)
    coefficient_order = tuple(
        sorted(coefficients, key=lambda value: (abs(value), value))
    )
    constant_order = tuple(
        sorted(constants, key=lambda value: (abs(value), value))
    )
    sample_domain = range(-sample_radius, sample_radius + 1)
    hypothesis_lhs, hypothesis_rhs, hypothesis_variables = hypothesis

    for parameters in product(
        coefficient_order,
        coefficient_order,
        constant_order,
        coefficient_order,
        coefficient_order,
        constant_order,
    ):
        model = _PGAPModel(*parameters)
        sampled = True
        for values in product(
            sample_domain, repeat=len(hypothesis_variables)
        ):
            environment = dict(zip(hypothesis_variables, values))
            if _pgap_evaluate_term(
                hypothesis_lhs, environment, model
            ) != _pgap_evaluate_term(
                hypothesis_rhs, environment, model
            ):
                sampled = False
                break
        if not sampled:
            continue
        if not _pgap_equation_holds_symbolically(hypothesis, model):
            continue
        witness = _pgap_counterexample_witness(
            goal, model, radius=witness_radius
        )
        if witness is not None:
            return model, witness, True
    return None, None, True


def _pgap_model_parameters(model):
    return (
        model.positive_left,
        model.positive_right,
        model.positive_constant,
        model.negative_left,
        model.negative_right,
        model.negative_constant,
    )


def _pgap_match_reflection_law(parsed_equation):
    """Recognize the action law certified by the constructor realization.

    The matcher is alpha-renaming and equality-orientation invariant.  It
    examines only the equation AST; no problem IDs, answer labels, or corpus
    metadata are consulted.
    """
    lhs, rhs, variables = parsed_equation

    def match_right(instance, schema):
        if schema[0] != OP:
            return None
        repeated, outer_tail = schema[1], schema[2]
        if outer_tail[0] != OP or outer_tail[2] != instance:
            return None
        selector = outer_tail[1]
        if selector[0] != OP:
            return None
        parameter, square = selector[1], selector[2]
        if square != (OP, repeated, repeated):
            return None
        return instance, repeated, parameter, False

    def match_left(instance, schema):
        if schema[0] != OP:
            return None
        outer_head, repeated = schema[1], schema[2]
        if outer_head[0] != OP or outer_head[1] != instance:
            return None
        selector = outer_head[2]
        if selector[0] != OP:
            return None
        square, parameter = selector[1], selector[2]
        if square != (OP, repeated, repeated):
            return None
        return instance, repeated, parameter, True

    for matcher in (match_right, match_left):
        forward = matcher(lhs, rhs)
        if forward is not None:
            return forward, False, variables
        reverse = matcher(rhs, lhs)
        if reverse is not None:
            return reverse, True, variables
    return None


def _pgap_render_carrier_value(value):
    if value >= 0:
        return "nonneg {}".format(value)
    return "negative {}".format(-value - 1)


def _pgap_render_constructor_term(term, operation_name="candidateOp"):
    """Render the inductive realization without redundant parentheses."""
    if term[0] == VAR:
        return term[1]

    def argument(child):
        rendered = _pgap_render_constructor_term(child, operation_name)
        return rendered if child[0] == VAR else "({})".format(rendered)

    return "{} {} {}".format(
        operation_name, argument(term[1]), argument(term[2])
    )


def _pgap_reflection_constructor_false_code(
    model, witness, hypothesis, goal
):
    """Compile the reflection PGAP to an axiom-free constructor proof.

    The carrier is a signed-natural inductive type.  Both guarded actions are
    definitional involutions, so the universal hypothesis is proved solely by
    constructor elimination and ``rfl``.  The concrete goal failure is closed
    by constructor disjointness.  The emitted target certificate is therefore
    accepted by the challenge's empty-axiom proof policy.
    """
    if _pgap_model_parameters(model) != (0, -1, 0, 0, -1, 1):
        return None
    match = _pgap_match_reflection_law(hypothesis)
    if match is None:
        return None
    (
        instance,
        repeated,
        parameter,
        opposite,
    ), reversed_equation, hypothesis_variables = match

    witness_values, lhs_value, rhs_value = witness
    if (lhs_value >= 0) == (rhs_value >= 0):
        # Constructor disjointness closes only opposite-sign witnesses.  Other
        # PGAP programs remain discoverable, but certificate emission fails
        # closed until a separately verified compiler is available.
        return None

    operation_name = "oppositeOp" if opposite else "candidateOp"
    magma_name = "oppositeMagma" if opposite else "candidateMagma"
    hypothesis_lhs = _pgap_render_constructor_term(
        hypothesis[0], operation_name
    )
    hypothesis_rhs = _pgap_render_constructor_term(
        hypothesis[1], operation_name
    )
    theorem_name = "opposite_source" if opposite else "candidate_source"
    source_proof = "{} {} {} {}".format(
        theorem_name,
        _pgap_render_constructor_term(instance, operation_name),
        _pgap_render_constructor_term(repeated, operation_name),
        _pgap_render_constructor_term(parameter, operation_name),
    )
    if reversed_equation:
        source_proof = "({}).symm".format(source_proof)
    witness_arguments = " ".join(
        "({})".format(_pgap_render_carrier_value(value))
        for value in witness_values
    )

    lines = [
        "import JudgeProblem",
        "",
        "namespace submission",
        "",
        "inductive CandidateCarrier",
        "  | nonneg : Nat → CandidateCarrier",
        "  | negative : Nat → CandidateCarrier",
        "",
        "open CandidateCarrier",
        "",
        "@[reducible] def reflectZero : CandidateCarrier → CandidateCarrier",
        "  | nonneg 0 => nonneg 0",
        "  | nonneg (Nat.succ n) => negative n",
        "  | negative n => nonneg (Nat.succ n)",
        "",
        "@[reducible] def reflectOne : CandidateCarrier → CandidateCarrier",
        "  | nonneg 0 => nonneg 1",
        "  | nonneg (Nat.succ 0) => nonneg 0",
        "  | nonneg (Nat.succ (Nat.succ n)) => negative n",
        "  | negative n => nonneg (Nat.succ (Nat.succ n))",
        "",
        "@[reducible] def candidateOp : CandidateCarrier → CandidateCarrier → CandidateCarrier",
        "  | nonneg _, right => reflectZero right",
        "  | negative _, right => reflectOne right",
        "",
        "@[reducible] def candidateMagma : Magma CandidateCarrier := {",
        "  op := candidateOp",
        "}",
        "",
        "@[reducible] def oppositeOp : CandidateCarrier → CandidateCarrier → CandidateCarrier :=",
        "  fun left right => candidateOp right left",
        "",
        "@[reducible] def oppositeMagma : Magma CandidateCarrier := {",
        "  op := oppositeOp",
        "}",
        "",
        "theorem reflectZero_twice (x : CandidateCarrier) : x = reflectZero (reflectZero x) := by",
        "  cases x with",
        "  | nonneg n =>",
        "      cases n with",
        "      | zero => rfl",
        "      | succ n => rfl",
        "  | negative n => rfl",
        "",
        "theorem reflectOne_twice (x : CandidateCarrier) : x = reflectOne (reflectOne x) := by",
        "  cases x with",
        "  | nonneg n =>",
        "      cases n with",
        "      | zero => rfl",
        "      | succ n =>",
        "          cases n with",
        "          | zero => rfl",
        "          | succ n => rfl",
        "  | negative n => rfl",
        "",
        "theorem candidate_source (x y z : CandidateCarrier) :",
        "    x = candidateOp y (candidateOp (candidateOp z (candidateOp y y)) x) := by",
        "  cases y with",
        "  | nonneg n =>",
        "      cases n with",
        "      | zero =>",
        "          cases z <;>",
        "            change x = reflectZero (reflectZero x) <;>",
        "            exact reflectZero_twice x",
        "      | succ n =>",
        "          cases z <;>",
        "            change x = reflectZero (reflectZero x) <;>",
        "            exact reflectZero_twice x",
        "  | negative n =>",
        "      cases z <;>",
        "        change x = reflectOne (reflectOne x) <;>",
        "        exact reflectOne_twice x",
        "",
        "theorem opposite_source (x y z : CandidateCarrier) :",
        "    x = oppositeOp (oppositeOp x (oppositeOp (oppositeOp y y) z)) y := by",
        "  change x = candidateOp y (candidateOp (candidateOp z (candidateOp y y)) x)",
        "  exact candidate_source x y z",
        "",
        "def proof : Goal := by",
        "  refine ⟨CandidateCarrier, {}, ?_, ?_⟩".format(magma_name),
        "  · change ∀ ({} : CandidateCarrier), {} = {}".format(
            " ".join(hypothesis_variables), hypothesis_lhs, hypothesis_rhs
        ),
        "    intro {}".format(" ".join(hypothesis_variables)),
        "    exact {}".format(source_proof),
        "  · intro claimed",
        "    have bad := claimed{}".format(
            (" " + witness_arguments) if witness_arguments else ""
        ),
        "    change {} = {} at bad".format(
            _pgap_render_carrier_value(lhs_value),
            _pgap_render_carrier_value(rhs_value),
        ),
        "    cases bad",
    ]
    lines.extend(
        [
            "",
            "end submission",
            "",
            "def submission : Goal := submission.proof",
        ]
    )
    return "\n".join(lines) + "\n"


def _pgap_render_int(value):
    return "({} : Int)".format(value)


def _pgap_render_term(term):
    if term[0] == VAR:
        return term[1]
    return "candidateOp ({}) ({})".format(
        _pgap_render_term(term[1]), _pgap_render_term(term[2])
    )


def make_polyhedral_guarded_action_false_code(
    model, witness, eq1_text, eq2_text
):
    """Compile only proof-policy-safe PGAP countermodels.

    Search remains general over the 729-program grammar.  Emission fails closed
    unless the synthesized program has an axiom-free constructor realization
    and the hypothesis matches a proven structural action law.  This separation
    preserves PGAP's discovery power without sending tactic-dependent or
    unverified certificates to the official Judge.
    """
    if model is None or witness is None:
        return None
    hypothesis = parse_equation(eq1_text)
    goal = parse_equation(eq2_text)
    if not _pgap_equation_holds_symbolically(hypothesis, model):
        return None
    witness_values, lhs_value, rhs_value = witness
    if lhs_value == rhs_value or len(witness_values) != len(goal[2]):
        return None
    environment = dict(zip(goal[2], witness_values))
    if _pgap_evaluate_term(goal[0], environment, model) == _pgap_evaluate_term(
        goal[1], environment, model
    ):
        return None
    code = _pgap_reflection_constructor_false_code(
        model, witness, hypothesis, goal
    )
    if code is None:
        return None
    if len(code.encode("utf-8")) > MAX_STRUCTURAL_FALSE_CERT_BYTES:
        return None
    return code


def _pgap_opposite_evaluate_term(term, environment, model):
    if term[0] == VAR:
        return environment[term[1]]
    left = _pgap_opposite_evaluate_term(term[1], environment, model)
    right = _pgap_opposite_evaluate_term(term[2], environment, model)
    return model.apply(right, left)


def dual_reflection_countermodel_code(eq1_text, eq2_text, radius=3):
    """Recover Candidate 23's operation-dual infinite reflection family."""
    hypothesis = parse_equation(eq1_text)
    matched = _pgap_match_reflection_law(hypothesis)
    if matched is None or not matched[0][3]:
        return None
    goal = parse_equation(eq2_text)
    model = _PGAPModel(0, -1, 0, 0, -1, 1)
    domain = tuple(
        sorted(range(-radius, radius + 1), key=lambda value: (abs(value), value))
    )
    for values in product(domain, repeat=len(goal[2])):
        environment = dict(zip(goal[2], values))
        lhs_value = _pgap_opposite_evaluate_term(goal[0], environment, model)
        rhs_value = _pgap_opposite_evaluate_term(goal[1], environment, model)
        if lhs_value == rhs_value or (lhs_value >= 0) == (rhs_value >= 0):
            continue
        witness = values, lhs_value, rhs_value
        code = _pgap_reflection_constructor_false_code(
            model, witness, hypothesis, goal
        )
        if code is not None and len(code.encode("utf-8")) <= (
            MAX_STRUCTURAL_FALSE_CERT_BYTES
        ):
            return code
    return None


def _match_pattern(pattern, target, substitution):
    if pattern[0] == VAR:
        name = pattern[1]
        previous = substitution.get(name)
        if previous is None:
            substitution[name] = target
            return True
        return previous == target
    if target[0] != OP:
        return False
    return _match_pattern(pattern[1], target[1], substitution) and _match_pattern(
        pattern[2], target[2], substitution
    )


def _instantiate(term, substitution):
    if term[0] == VAR:
        return substitution[term[1]]
    return (
        OP,
        _instantiate(term[1], substitution),
        _instantiate(term[2], substitution),
    )


def _direct_instance(eq1, eq2):
    h_lhs, h_rhs, h_variables = eq1
    goal_lhs, goal_rhs, _ = eq2
    for symmetric, target_lhs, target_rhs in (
        (False, goal_lhs, goal_rhs),
        (True, goal_rhs, goal_lhs),
    ):
        substitution = {}
        if not _match_pattern(h_lhs, target_lhs, substitution):
            continue
        if not _match_pattern(h_rhs, target_rhs, substitution):
            continue
        if any(variable not in substitution for variable in h_variables):
            continue
        return substitution, symmetric
    return None


def _intro_line(variables):
    if variables:
        return "intro {}".format(" ".join(variables))
    return ""


def reflexive_proof(eq2_text):
    lhs, rhs, variables = parse_equation(eq2_text)
    if lhs != rhs:
        return None
    lines = [_intro_line(variables), "rfl"]
    return "\n".join(line for line in lines if line)


def direct_substitution_proof(eq1_text, eq2_text):
    eq1 = parse_equation(eq1_text)
    eq2 = parse_equation(eq2_text)
    match = _direct_instance(eq1, eq2)
    if match is None:
        return None
    substitution, symmetric = match
    arguments = " ".join(
        render_term(substitution[variable]) for variable in eq1[2]
    )
    application = "hyp" + ((" " + arguments) if arguments else "")
    if symmetric:
        application = "({}).symm".format(application)
    lines = [_intro_line(eq2[2]), "exact {}".format(application)]
    return "\n".join(line for line in lines if line)


def singleton_collapse_proof(eq1_text, eq2_text):
    h_lhs, h_rhs, h_variables = parse_equation(eq1_text)
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if not goal_variables:
        return None

    isolated = None
    isolated_on_left = False
    if h_lhs[0] == VAR and h_lhs[1] not in variables_set(h_rhs):
        isolated = h_lhs[1]
        isolated_on_left = True
    elif h_rhs[0] == VAR and h_rhs[1] not in variables_set(h_lhs):
        isolated = h_rhs[1]
        isolated_on_left = False
    if isolated is None:
        return None

    filler = (VAR, goal_variables[0])

    def application(replacement):
        terms = []
        for variable in h_variables:
            terms.append(replacement if variable == isolated else filler)
        rendered = " ".join(render_term(term) for term in terms)
        return "hyp" + ((" " + rendered) if rendered else "")

    app_a = application((VAR, "sa"))
    app_b = application((VAR, "sb"))
    if isolated_on_left:
        equality = "({}).trans ({}).symm".format(app_a, app_b)
    else:
        equality = "({}).symm.trans ({})".format(app_a, app_b)

    lines = [
        _intro_line(goal_variables),
        "have all_eq : ∀ (sa sb : G), sa = sb := by",
        "  intro sa sb",
        "  exact {}".format(equality),
        "exact all_eq {} {}".format(render_term(goal_lhs), render_term(goal_rhs)),
    ]
    return "\n".join(line for line in lines if line)


def _walk_paths(term, path=()):
    yield path, term
    if term[0] == OP:
        yield from _walk_paths(term[1], path + (0,))
        yield from _walk_paths(term[2], path + (1,))


def _replace_at_path(term, path, replacement):
    if not path:
        return replacement
    if path[0] == 0:
        return (
            OP,
            _replace_at_path(term[1], path[1:], replacement),
            term[2],
        )
    return (
        OP,
        term[1],
        _replace_at_path(term[2], path[1:], replacement),
    )


def _wrap_congruence(root, path, inner_proof):
    ancestors = []
    node = root
    for direction in path:
        ancestors.append((node, direction))
        node = node[1] if direction == 0 else node[2]
    proof = inner_proof
    for ancestor, direction in reversed(ancestors):
        if direction == 0:
            function = "fun t => t ◇ {}".format(render_term(ancestor[2]))
        else:
            function = "fun t => {} ◇ t".format(render_term(ancestor[1]))
        proof = "congrArg ({}) ({})".format(function, proof)
    return proof


def _paramod_dereference(term, substitution):
    seen = set()
    while term[0] == VAR and term[1] in substitution:
        if term[1] in seen:
            break
        seen.add(term[1])
        term = substitution[term[1]]
    return term


def _paramod_resolve(term, substitution):
    term = _paramod_dereference(term, substitution)
    if term[0] == OP:
        return (
            OP,
            _paramod_resolve(term[1], substitution),
            _paramod_resolve(term[2], substitution),
        )
    return term


def _paramod_occurs(variable, term, substitution):
    term = _paramod_dereference(term, substitution)
    if term[0] == VAR:
        return term[1] == variable
    return term[0] == OP and (
        _paramod_occurs(variable, term[1], substitution)
        or _paramod_occurs(variable, term[2], substitution)
    )


def _paramod_unify(left, right, substitution):
    left = _paramod_dereference(left, substitution)
    right = _paramod_dereference(right, substitution)
    if left == right:
        return True
    if left[0] == VAR:
        if _paramod_occurs(left[1], right, substitution):
            return False
        substitution[left[1]] = right
        return True
    if right[0] == VAR:
        if _paramod_occurs(right[1], left, substitution):
            return False
        substitution[right[1]] = left
        return True
    return (
        left[0] == OP
        and right[0] == OP
        and _paramod_unify(left[1], right[1], substitution)
        and _paramod_unify(left[2], right[2], substitution)
    )


def _paramod_rename(term, prefix):
    if term[0] == VAR:
        return (VAR, prefix + term[1])
    return (
        OP,
        _paramod_rename(term[1], prefix),
        _paramod_rename(term[2], prefix),
    )


def _paramod_canonicalize(left, right):
    def build(first, second):
        names = {}

        def visit(term):
            if term[0] == VAR:
                if term[1] not in names:
                    names[term[1]] = "v{}".format(len(names))
                return (VAR, names[term[1]])
            return (OP, visit(term[1]), visit(term[2]))

        return (visit(first), visit(second)), names

    forward, forward_names = build(left, right)
    reverse, reverse_names = build(right, left)
    if repr(forward) <= repr(reverse):
        return forward, forward_names, False
    return reverse, reverse_names, True


def _paramod_map_variables(term, names, filler):
    if term[0] == VAR:
        return (VAR, names.get(term[1], filler[1]))
    return (
        OP,
        _paramod_map_variables(term[1], names, filler),
        _paramod_map_variables(term[2], names, filler),
    )


def _paramod_is_singleton(equation):
    return (
        equation[0][0] == VAR
        and equation[1][0] == VAR
        and equation[0] != equation[1]
    )


def _paramod_goal_match(equation, parsed_goal):
    return _direct_instance(
        (equation[0], equation[1], variables_in_order(*equation)),
        parsed_goal,
    )


def _paramod_term_distance(left, right):
    if left == right:
        return 0
    if left[0] != right[0]:
        return 1 + term_size(left) + term_size(right)
    if left[0] == VAR:
        return 1
    return _paramod_term_distance(
        left[1], right[1]
    ) + _paramod_term_distance(left[2], right[2])


def _paramod_pattern_distance(pattern, target, substitution):
    """Return a deterministic distance from a rule pattern to a goal term."""
    if pattern[0] == VAR:
        previous = substitution.get(pattern[1])
        if previous is None:
            substitution[pattern[1]] = target
            return 0
        return _paramod_term_distance(previous, target)
    if target[0] != OP:
        return 1 + term_size(pattern)
    return _paramod_pattern_distance(
        pattern[1], target[1], substitution
    ) + _paramod_pattern_distance(pattern[2], target[2], substitution)


def _paramod_goal_distance(equation, parsed_goal):
    goal_lhs, goal_rhs, _ = parsed_goal
    distances = []
    for target_lhs, target_rhs in (
        (goal_lhs, goal_rhs),
        (goal_rhs, goal_lhs),
    ):
        substitution = {}
        distances.append(
            _paramod_pattern_distance(
                equation[0], target_lhs, substitution
            )
            + _paramod_pattern_distance(
                equation[1], target_rhs, substitution
            )
        )
    return min(distances)


def _paramod_score(equation, depth, parsed_goal=None):
    return (
        0
        if parsed_goal is not None
        and _paramod_goal_match(equation, parsed_goal) is not None
        else (1 if _paramod_is_singleton(equation) else 2),
        0
        if parsed_goal is None
        else _paramod_goal_distance(equation, parsed_goal),
        depth,
        max(term_size(equation[0]), term_size(equation[1])),
        term_size(equation[0]) + term_size(equation[1]),
        repr(equation),
    )


def _paramod_application(rule_index, arguments, symmetric):
    rendered = " ".join(render_term(term) for term in arguments)
    result = "h{}".format(rule_index)
    if rendered:
        result += " " + rendered
    result = "({})".format(result)
    if symmetric:
        result += ".symm"
    return result


def _paramodulations(
    outer_index,
    inner_index,
    outer,
    inner,
    serial,
    max_term_size,
):
    """Yield proof-producing, variable-standardized paramodulation steps."""
    outer_prefix = "o{}_".format(serial)
    inner_prefix = "i{}_".format(serial)
    outer_terms = (
        _paramod_rename(outer[0], outer_prefix),
        _paramod_rename(outer[1], outer_prefix),
    )
    inner_terms = (
        _paramod_rename(inner[0], inner_prefix),
        _paramod_rename(inner[1], inner_prefix),
    )
    outer_variables = variables_in_order(*outer)
    inner_variables = variables_in_order(*inner)

    for outer_side in (0, 1):
        outer_source = outer_terms[outer_side]
        outer_other = outer_terms[1 - outer_side]
        for inner_side in (0, 1):
            inner_source = inner_terms[inner_side]
            inner_other = inner_terms[1 - inner_side]
            for path, subtree in _walk_paths(outer_source):
                if subtree[0] == VAR:
                    continue
                substitution = {}
                if not _paramod_unify(subtree, inner_source, substitution):
                    continue
                source = _paramod_resolve(outer_source, substitution)
                replacement = _paramod_resolve(inner_other, substitution)
                replaced = _paramod_resolve(
                    _replace_at_path(source, path, replacement), substitution
                )
                other = _paramod_resolve(outer_other, substitution)
                if replaced == other or max(
                    term_size(replaced), term_size(other)
                ) > max_term_size:
                    continue

                equation, names, swapped = _paramod_canonicalize(
                    other, replaced
                )
                child_variables = variables_in_order(*equation)
                if not child_variables:
                    continue
                filler = (VAR, child_variables[0])
                canonical_source = _paramod_map_variables(
                    source, names, filler
                )
                outer_arguments = [
                    _paramod_map_variables(
                        _paramod_resolve(
                            (VAR, outer_prefix + variable), substitution
                        ),
                        names,
                        filler,
                    )
                    for variable in outer_variables
                ]
                inner_arguments = [
                    _paramod_map_variables(
                        _paramod_resolve(
                            (VAR, inner_prefix + variable), substitution
                        ),
                        names,
                        filler,
                    )
                    for variable in inner_variables
                ]
                outer_proof = _paramod_application(
                    outer_index, outer_arguments, outer_side == 1
                )
                inner_proof = _paramod_application(
                    inner_index, inner_arguments, inner_side == 1
                )
                inner_wrapped = _wrap_congruence(
                    canonical_source, path, inner_proof
                )
                proof = "({}).symm.trans ({})".format(
                    outer_proof, inner_wrapped
                )
                if swapped:
                    proof = "({}).symm".format(proof)
                yield equation, proof, (outer_index, inner_index)


def _paramod_initial_proof(parsed_hypothesis, initial):
    target = (initial[0], initial[1], variables_in_order(*initial))
    match = _direct_instance(parsed_hypothesis, target)
    if match is None:
        return None
    substitution, symmetric = match
    rendered = " ".join(
        render_term(substitution[variable]) for variable in parsed_hypothesis[2]
    )
    proof = "hyp" + ((" " + rendered) if rendered else "")
    if symmetric:
        proof = "({}).symm".format(proof)
    return proof


def _paramod_rule_replays(
    index,
    parsed_hypothesis,
    rules,
    proofs,
    parents,
    max_term_size,
):
    """Rebuild one proof-DAG node from AST parents, failing closed."""
    if not (0 <= index < len(rules)):
        return False
    if len(rules) != len(proofs) or len(rules) != len(parents):
        return False
    if index == 0:
        return (
            parents[0] is None
            and proofs[0] == _paramod_initial_proof(parsed_hypothesis, rules[0])
        )
    source = parents[index]
    if (
        not isinstance(source, tuple)
        or len(source) != 2
        or not all(isinstance(parent, int) for parent in source)
        or not all(0 <= parent < index for parent in source)
    ):
        return False
    for equation, proof, replay_source in _paramodulations(
        source[0],
        source[1],
        rules[source[0]],
        rules[source[1]],
        index,
        max_term_size,
    ):
        if (
            equation == rules[index]
            and proof == proofs[index]
            and replay_source == source
        ):
            return True
    return False


def _render_paramod_goal_proof(
    eq2_text,
    parsed_hypothesis,
    rules,
    proofs,
    parents,
    goal_index,
    max_term_size,
):
    if (
        len(rules) != len(proofs)
        or len(rules) != len(parents)
        or not isinstance(goal_index, int)
        or not (0 <= goal_index < len(rules))
    ):
        return None
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if not goal_variables:
        return None
    parsed_goal = (goal_lhs, goal_rhs, goal_variables)
    match = _paramod_goal_match(rules[goal_index], parsed_goal)
    if match is None:
        return None
    substitution, symmetric = match
    needed = set()
    visiting = set()
    valid = True

    def include(index):
        nonlocal valid
        if not valid or index in needed:
            return
        if not isinstance(index, int) or not (0 <= index < len(rules)):
            valid = False
            return
        if index in visiting:
            valid = False
            return
        visiting.add(index)
        needed.add(index)
        source = parents[index]
        if source is not None:
            if not isinstance(source, tuple) or len(source) != 2:
                valid = False
                visiting.discard(index)
                return
            include(source[0])
            include(source[1])
        visiting.discard(index)

    include(goal_index)
    if not valid:
        return None
    for index in sorted(needed):
        if not _paramod_rule_replays(
            index,
            parsed_hypothesis,
            rules,
            proofs,
            parents,
            max_term_size,
        ):
            return None
    lines = [_intro_line(goal_variables)]
    for index in sorted(needed):
        equation = rules[index]
        variables = variables_in_order(*equation)
        if not variables:
            return None
        lines.append(
            "have h{} ({} : G) : {} = {} := by".format(
                index,
                " ".join(variables),
                render_term(equation[0]),
                render_term(equation[1]),
            )
        )
        lines.append("  exact {}".format(proofs[index]))
    rule_variables = variables_in_order(*rules[goal_index])
    if any(variable not in substitution for variable in rule_variables):
        return None
    arguments = " ".join(
        render_term(substitution[variable]) for variable in rule_variables
    )
    exact = "h{}".format(goal_index)
    if arguments:
        exact += " " + arguments
    if symmetric:
        exact = "({}).symm".format(exact)
    lines.append("exact {}".format(exact))
    return "\n".join(line for line in lines if line)


def _bounded_paramodulation_proof(
    eq1_text,
    eq2_text,
    max_depth,
    max_rules,
    max_candidates,
    max_queue,
    max_term_size,
    stop_at_goal,
):
    """Run the shared, proof-producing bounded paramodulation engine.

    This is a bounded implementation of standard paramodulation: variables in
    the two parent equations are renamed apart, a non-variable subterm is
    unified with either side of the second equation, and the resulting proof
    is reconstructed from congruence, symmetry, and transitivity.  Every
    selected proof-DAG node is replayed from its AST parents before Lean is
    emitted.  The public method references are the Apache-2.0 Equational
    Theories superposition reconstruction and generated Vampire proofs; no
    theorem table or problem identifier is embedded here.
    """
    parsed_hypothesis = parse_equation(eq1_text)
    parsed_goal = parse_equation(eq2_text)
    if max(term_size(parsed_hypothesis[0]), term_size(parsed_hypothesis[1])) > (
        max_term_size
    ):
        return None
    initial, _, _ = _paramod_canonicalize(
        parsed_hypothesis[0], parsed_hypothesis[1]
    )
    initial_proof = _paramod_initial_proof(parsed_hypothesis, initial)
    if initial_proof is None:
        return None

    rules = [initial]
    proofs = [initial_proof]
    parents = [None]
    depths = [0]
    keys = {initial}
    queued = set()
    candidates = []
    serial = 0
    ordinal = 0

    def enqueue_pair(outer_index, inner_index):
        nonlocal serial, ordinal
        depth = max(depths[outer_index], depths[inner_index]) + 1
        if depth > max_depth or len(queued) >= max_queue:
            return
        serial += 1
        for equation, proof, source in _paramodulations(
            outer_index,
            inner_index,
            rules[outer_index],
            rules[inner_index],
            serial,
            max_term_size,
        ):
            if equation in keys or equation in queued:
                continue
            if (
                stop_at_goal
                and _paramod_goal_match(equation, parsed_goal) is not None
            ):
                return equation, depth, proof, source
            if len(queued) >= max_queue:
                break
            queued.add(equation)
            ordinal += 1
            heapq.heappush(
                candidates,
                (
                    _paramod_score(
                        equation,
                        depth,
                        parsed_goal if stop_at_goal else None,
                    ),
                    ordinal,
                    equation,
                    depth,
                    proof,
                    source,
                ),
            )
        return None

    def render_generated_goal(candidate):
        if len(rules) >= max_rules:
            return None
        equation, depth, proof, source = candidate
        keys.add(equation)
        rules.append(equation)
        proofs.append(proof)
        parents.append(source)
        depths.append(depth)
        return _render_paramod_goal_proof(
            eq2_text,
            parsed_hypothesis,
            rules,
            proofs,
            parents,
            len(rules) - 1,
            max_term_size,
        )

    if (
        _paramod_goal_match(initial, parsed_goal) is not None
        if stop_at_goal
        else _paramod_is_singleton(initial)
    ):
        return _render_paramod_goal_proof(
            eq2_text,
            parsed_hypothesis,
            rules,
            proofs,
            parents,
            0,
            max_term_size,
        )

    generated_goal = enqueue_pair(0, 0)
    if generated_goal is not None:
        return render_generated_goal(generated_goal)
    processed = 0
    while candidates and len(rules) < max_rules and processed < max_candidates:
        _, _, equation, depth, proof, source = heapq.heappop(candidates)
        queued.discard(equation)
        processed += 1
        if equation in keys:
            continue
        keys.add(equation)
        rules.append(equation)
        proofs.append(proof)
        parents.append(source)
        depths.append(depth)
        new_index = len(rules) - 1
        if (
            _paramod_goal_match(equation, parsed_goal) is not None
            if stop_at_goal
            else _paramod_is_singleton(equation)
        ):
            return _render_paramod_goal_proof(
                eq2_text,
                parsed_hypothesis,
                rules,
                proofs,
                parents,
                new_index,
                max_term_size,
            )
        for old_index in range(new_index + 1):
            generated_goal = enqueue_pair(new_index, old_index)
            if generated_goal is not None:
                return render_generated_goal(generated_goal)
            if old_index != new_index:
                generated_goal = enqueue_pair(old_index, new_index)
                if generated_goal is not None:
                    return render_generated_goal(generated_goal)
    return None


def derived_singleton_paramodulation_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_DERIVED_SINGLETON_DEPTH,
    max_rules=MAX_DERIVED_SINGLETON_RULES,
    max_candidates=MAX_DERIVED_SINGLETON_CANDIDATES,
    max_queue=MAX_DERIVED_SINGLETON_QUEUE,
    max_term_size=MAX_DERIVED_SINGLETON_TERM_SIZE,
):
    """Derive a universal singleton law with the original fixed bounds."""
    return _bounded_paramodulation_proof(
        eq1_text,
        eq2_text,
        max_depth=max_depth,
        max_rules=max_rules,
        max_candidates=max_candidates,
        max_queue=max_queue,
        max_term_size=max_term_size,
        stop_at_goal=False,
    )


def goal_directed_paramodulation_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_GOAL_PARAMOD_DEPTH,
    max_rules=MAX_GOAL_PARAMOD_RULES,
    max_candidates=MAX_GOAL_PARAMOD_CANDIDATES,
    max_queue=MAX_GOAL_PARAMOD_QUEUE,
    max_term_size=MAX_GOAL_PARAMOD_TERM_SIZE,
):
    """Prove a direct or reverse goal instance with fixed saturation caps."""
    return _bounded_paramodulation_proof(
        eq1_text,
        eq2_text,
        max_depth=max_depth,
        max_rules=max_rules,
        max_candidates=max_candidates,
        max_queue=max_queue,
        max_term_size=max_term_size,
        stop_at_goal=True,
    )


def late_goal_directed_paramodulation_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_LATE_GOAL_PARAMOD_DEPTH,
    max_rules=MAX_LATE_GOAL_PARAMOD_RULES,
    max_candidates=MAX_LATE_GOAL_PARAMOD_CANDIDATES,
    max_queue=MAX_LATE_GOAL_PARAMOD_QUEUE,
    max_term_size=MAX_LATE_GOAL_PARAMOD_TERM_SIZE,
):
    """Retry the same proof engine with larger fixed bounds on the final tail."""
    return _bounded_paramodulation_proof(
        eq1_text,
        eq2_text,
        max_depth=max_depth,
        max_rules=max_rules,
        max_candidates=max_candidates,
        max_queue=max_queue,
        max_term_size=max_term_size,
        stop_at_goal=True,
    )


def deep_goal_directed_paramodulation_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_DEEP_GOAL_PARAMOD_DEPTH,
    max_rules=MAX_DEEP_GOAL_PARAMOD_RULES,
    max_candidates=MAX_DEEP_GOAL_PARAMOD_CANDIDATES,
    max_queue=MAX_DEEP_GOAL_PARAMOD_QUEUE,
    max_term_size=MAX_DEEP_GOAL_PARAMOD_TERM_SIZE,
):
    """Run one final bounded goal search for the difficult true tail."""
    return _bounded_paramodulation_proof(
        eq1_text,
        eq2_text,
        max_depth=max_depth,
        max_rules=max_rules,
        max_candidates=max_candidates,
        max_queue=max_queue,
        max_term_size=max_term_size,
        stop_at_goal=True,
    )

def extended_goal_directed_paramodulation_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_EXTENDED_GOAL_PARAMOD_DEPTH,
    max_rules=MAX_EXTENDED_GOAL_PARAMOD_RULES,
    max_candidates=MAX_EXTENDED_GOAL_PARAMOD_CANDIDATES,
    max_queue=MAX_EXTENDED_GOAL_PARAMOD_QUEUE,
    max_term_size=MAX_EXTENDED_GOAL_PARAMOD_TERM_SIZE,
):
    """Run one larger replay-checked search after the bounded deep miss."""
    return _bounded_paramodulation_proof(
        eq1_text,
        eq2_text,
        max_depth=max_depth,
        max_rules=max_rules,
        max_candidates=max_candidates,
        max_queue=max_queue,
        max_term_size=max_term_size,
        stop_at_goal=True,
    )

PRODUCT_COLLAPSE_GOAL = "a ◇ b = c ◇ d"
PRODUCT_COLLAPSE_SEPARATED_BRIDGE = "a ◇ b = c ◇ (d ◇ e)"
PRODUCT_COLLAPSE_SHARED_LEFT_BRIDGE = "a ◇ b = c ◇ (a ◇ (d ◇ c))"


def _term_variable_occurrences(term, variable):
    if term[0] == VAR:
        return int(term[1] == variable)
    if term[0] == OP:
        return _term_variable_occurrences(
            term[1], variable
        ) + _term_variable_occurrences(term[2], variable)
    return 0


def _generic_product_bridge_shape(eq1_text):
    lhs, rhs, _ = parse_equation(eq1_text)
    for generic, other in ((lhs, rhs), (rhs, lhs)):
        if (
            generic[0] == OP
            and generic[1][0] == VAR
            and generic[2][0] == VAR
            and generic[1][1] != generic[2][1]
            and other[0] == OP
        ):
            return generic[1][1], generic[2][1], other
    return None


def _nested_proof_lines(proof_body):
    return [
        "  " + line if line.strip() else ""
        for line in proof_body.strip().splitlines()
    ]


def _render_direct_product_collapse(goal_lhs, goal_rhs, goal_variables, proof):
    lines = [_intro_line(goal_variables)]
    lines.append(
        "have collapse : ∀ (a b c d : G), a ◇ b = c ◇ d := by"
    )
    lines.extend(_nested_proof_lines(proof))
    lines.append(
        "exact collapse {} {} {} {}".format(
            render_term(goal_lhs[1]),
            render_term(goal_lhs[2]),
            render_term(goal_rhs[1]),
            render_term(goal_rhs[2]),
        )
    )
    return "\n".join(line for line in lines if line)


def _render_separated_product_bridge(
    goal_lhs, goal_rhs, goal_variables, proof
):
    lines = [_intro_line(goal_variables)]
    lines.append(
        "have bridge : ∀ (a b c d e : G), "
        "a ◇ b = c ◇ (d ◇ e) := by"
    )
    lines.extend(_nested_proof_lines(proof))
    lhs_a = render_term(goal_lhs[1])
    lhs_b = render_term(goal_lhs[2])
    rhs_a = render_term(goal_rhs[1])
    rhs_b = render_term(goal_rhs[2])
    lines.append(
        "exact (bridge {} {} {} {} {}).trans "
        "((bridge {} {} {} {} {}).symm)".format(
            lhs_a,
            lhs_b,
            rhs_a,
            rhs_b,
            rhs_b,
            rhs_a,
            rhs_b,
            rhs_a,
            rhs_b,
            rhs_b,
        )
    )
    return "\n".join(line for line in lines if line)


def _render_shared_left_product_bridge(
    goal_lhs, goal_rhs, goal_variables, proof
):
    lines = [_intro_line(goal_variables)]
    lines.append(
        "have bridge : ∀ (a b c d : G), "
        "a ◇ b = c ◇ (a ◇ (d ◇ c)) := by"
    )
    lines.extend(_nested_proof_lines(proof))
    lhs_a = render_term(goal_lhs[1])
    lhs_b = render_term(goal_lhs[2])
    rhs_a = render_term(goal_rhs[1])
    rhs_b = render_term(goal_rhs[2])
    lines.extend(
        [
            "calc",
            "  ({} ◇ {}) = ({} ◇ ({} ◇ ({} ◇ {}))) := "
            "(bridge {} {} {} {})".format(
                lhs_a,
                lhs_b,
                lhs_a,
                lhs_a,
                lhs_a,
                lhs_a,
                lhs_a,
                lhs_b,
                lhs_a,
                lhs_a,
            ),
            "  _ = ({} ◇ ({} ◇ ({} ◇ {}))) := "
            "((bridge {} ({} ◇ ({} ◇ {})) {} {}).symm)".format(
                lhs_a,
                rhs_a,
                lhs_a,
                lhs_a,
                lhs_a,
                rhs_a,
                lhs_a,
                lhs_a,
                lhs_a,
                lhs_a,
            ),
            "  _ = ({} ◇ {}) := ((bridge {} {} {} {}).symm)".format(
                rhs_a,
                rhs_b,
                rhs_a,
                rhs_b,
                lhs_a,
                lhs_a,
            ),
        ]
    )
    return "\n".join(line for line in lines if line)


def product_collapse_bridge_proof(eq1_text, eq2_text):
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if (
        not goal_variables
        or goal_lhs[0] != OP
        or goal_rhs[0] != OP
    ):
        return None
    shape = _generic_product_bridge_shape(eq1_text)
    if shape is None:
        return None

    direct = deep_goal_directed_paramodulation_proof(
        eq1_text, PRODUCT_COLLAPSE_GOAL
    )
    if direct:
        return _render_direct_product_collapse(
            goal_lhs, goal_rhs, goal_variables, direct
        )

    first_variable, second_variable, other = shape
    first_count = _term_variable_occurrences(other, first_variable)
    second_count = _term_variable_occurrences(other, second_variable)
    if first_count > second_count:
        bridge_goal = PRODUCT_COLLAPSE_SHARED_LEFT_BRIDGE
        renderer = _render_shared_left_product_bridge
    else:
        bridge_goal = PRODUCT_COLLAPSE_SEPARATED_BRIDGE
        renderer = _render_separated_product_bridge

    bridge = extended_goal_directed_paramodulation_proof(
        eq1_text, bridge_goal
    )
    if not bridge:
        return None
    return renderer(goal_lhs, goal_rhs, goal_variables, bridge)

def _hypothesis_has_variable_side(eq1_text):
    lhs, rhs, _ = parse_equation(eq1_text)
    return lhs[0] == VAR or rhs[0] == VAR

DISTILLED_RIGHT_PROJECTION_SOURCE = "x = ((y ◇ (x ◇ z)) ◇ y) ◇ x"
DISTILLED_LEFT_INSENSITIVE_SOURCE = "x ◇ y = y ◇ (x ◇ (z ◇ y))"

# This ID-free proof body is distilled from a pinned public ETP equality DAG.
# It uses only hyp, congrArg, rfl, transitivity, and symmetry, and every emitted
# candidate still passes through the organizer's normal Lean judge.
DISTILLED_RIGHT_PROJECTION_LAW_PROOF = r"""intro y x
have h0 (v0 v1 v2 : G) : (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v1) = v1 := by
  exact (hyp v1 v0 v2).symm
have h1 (v0 v1 v2 v3 : G) : (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ (v1 ◇ v3)) ◇ v2)) = ((v2 ◇ (v1 ◇ v3)) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ (v1 ◇ v3)) ◇ v2)) ((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ (((v2 ◇ (v1 ◇ v3)) ◇ v2) ◇ v1)) (rfl)).trans (congrArg (fun q => v0 ◇ q) ((h0 v2 v1 v3))))).trans (congrArg (fun q => (v0 ◇ v1) ◇ q) (rfl)))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h0 v0 ((v2 ◇ (v1 ◇ v3)) ◇ v2) v1)).trans (rfl))
have h2 (v0 v1 v2 v3 : G) : (((v0 ◇ v1) ◇ ((v2 ◇ ((v0 ◇ v1) ◇ v3)) ◇ v2)) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ ((v2 ◇ ((v0 ◇ v1) ◇ v3)) ◇ v2)) ((h0 v2 (v0 ◇ v1) v3))).trans (congrArg (fun q => (v0 ◇ v1) ◇ q) (rfl)))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ ((v2 ◇ ((v0 ◇ v1) ◇ v3)) ◇ v2)) ◇ q) (rfl))).symm).trans (((h0 ((v2 ◇ ((v0 ◇ v1) ◇ v3)) ◇ v2) v0 v1)).trans (rfl))
have h3 (v0 v1 v2 v3 v4 : G) : ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v3 ◇ (v0 ◇ v4)) ◇ v3)) = ((v3 ◇ (v0 ◇ v4)) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ (v0 ◇ v4)) ◇ v3)) ((congrArg (fun q => q ◇ ((v1 ◇ ((((v3 ◇ (v0 ◇ v4)) ◇ v3) ◇ v0) ◇ v2)) ◇ v1)) ((h0 v3 v0 v4))).trans (congrArg (fun q => v0 ◇ q) ((congrArg (fun q => q ◇ v1) ((congrArg (fun q => q ◇ ((((v3 ◇ (v0 ◇ v4)) ◇ v3) ◇ v0) ◇ v2)) (rfl)).trans (congrArg (fun q => v1 ◇ q) ((congrArg (fun q => q ◇ v2) ((h0 v3 v0 v4))).trans (congrArg (fun q => v0 ◇ q) (rfl)))))).trans (congrArg (fun q => (v1 ◇ (v0 ◇ v2)) ◇ q) (rfl)))))).trans (congrArg (fun q => (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ q) (rfl))).symm).trans (((h2 ((v3 ◇ (v0 ◇ v4)) ◇ v3) v0 v1 v2)).trans (rfl))
have h4 (v0 v1 v2 v3 : G) : ((((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) ◇ (v0 ◇ (v1 ◇ v2))) = (v0 ◇ (v1 ◇ v2)) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ (v1 ◇ v2))) ((congrArg (fun q => q ◇ ((v3 ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v1)) ◇ v3)) (rfl)).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v1)) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((h0 v0 v1 v2))))).trans (congrArg (fun q => (v3 ◇ v1) ◇ q) (rfl)))))).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) ◇ q) (rfl))).symm).trans (((h2 (v0 ◇ (v1 ◇ v2)) v0 v3 v1)).trans (rfl))
have h5 (v0 v1 v2 v3 v4 v5 : G) : ((((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) ◇ ((v4 ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v5)) ◇ v4)) = ((v4 ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v5)) ◇ v4) := by
  exact (((congrArg (fun q => q ◇ ((v4 ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v5)) ◇ v4)) ((congrArg (fun q => q ◇ ((v3 ◇ v1) ◇ v3)) ((h1 v3 v1 v0 v2))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) (rfl)))).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) ◇ q) (rfl))).symm).trans (((h1 ((v3 ◇ v1) ◇ v3) ((v0 ◇ (v1 ◇ v2)) ◇ v0) v4 v5)).trans (rfl))
have h6 (v0 v1 v2 v3 : G) : (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ ((v2 ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v3)) ◇ v2)) = ((v2 ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v3)) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v3)) ◇ v2)) ((h1 (v0 ◇ (v0 ◇ v1)) v0 v0 v1))).trans (congrArg (fun q => ((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h1 ((v0 ◇ (v0 ◇ v1)) ◇ v0) (v0 ◇ (v0 ◇ v1)) v2 v3)).trans (rfl))
have h7 (v0 v1 v2 v3 v4 : G) : (((v0 ◇ ((v1 ◇ (v2 ◇ v3)) ◇ v1)) ◇ v0) ◇ ((v4 ◇ v2) ◇ v4)) = ((v4 ◇ v2) ◇ v4) := by
  exact (((congrArg (fun q => q ◇ ((v4 ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ v2)) ◇ v4)) (rfl)).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v2 ◇ v3)) ◇ v1)) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ v4) ((congrArg (fun q => q ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ v2)) (rfl)).trans (congrArg (fun q => v4 ◇ q) ((h0 v1 v2 v3))))).trans (congrArg (fun q => (v4 ◇ v2) ◇ q) (rfl))))).symm).trans (((h1 v0 ((v1 ◇ (v2 ◇ v3)) ◇ v1) v4 v2)).trans ((congrArg (fun q => q ◇ v4) ((congrArg (fun q => q ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ v2)) (rfl)).trans (congrArg (fun q => v4 ◇ q) ((h0 v1 v2 v3))))).trans (congrArg (fun q => (v4 ◇ v2) ◇ q) (rfl))))
have h8 (v0 v1 v2 v3 v4 v5 : G) : (((v0 ◇ ((v1 ◇ v2) ◇ v1)) ◇ v0) ◇ ((v3 ◇ ((v4 ◇ (v2 ◇ v5)) ◇ v4)) ◇ v3)) = ((v3 ◇ ((v4 ◇ (v2 ◇ v5)) ◇ v4)) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ (((v1 ◇ v2) ◇ v1) ◇ ((v4 ◇ (v2 ◇ v5)) ◇ v4))) ◇ v3)) (rfl)).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ v2) ◇ v1)) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ (((v1 ◇ v2) ◇ v1) ◇ ((v4 ◇ (v2 ◇ v5)) ◇ v4))) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((h1 v1 v2 v4 v5))))).trans (congrArg (fun q => (v3 ◇ ((v4 ◇ (v2 ◇ v5)) ◇ v4)) ◇ q) (rfl))))).symm).trans (((h1 v0 ((v1 ◇ v2) ◇ v1) v3 ((v4 ◇ (v2 ◇ v5)) ◇ v4))).trans ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ (((v1 ◇ v2) ◇ v1) ◇ ((v4 ◇ (v2 ◇ v5)) ◇ v4))) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((h1 v1 v2 v4 v5))))).trans (congrArg (fun q => (v3 ◇ ((v4 ◇ (v2 ◇ v5)) ◇ v4)) ◇ q) (rfl))))
have h9 (v0 v1 v2 v3 v4 : G) : (((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v4 ◇ v2) ◇ v4))) = (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v4 ◇ v2) ◇ v4)) := by
  exact (((congrArg (fun q => q ◇ ((((v4 ◇ v2) ◇ v4) ◇ ((v1 ◇ (v2 ◇ v3)) ◇ v1)) ◇ ((v4 ◇ v2) ◇ v4))) (rfl)).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ ((v4 ◇ v2) ◇ v4)) ((h1 v4 v2 v1 v3))).trans (congrArg (fun q => ((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ q) (rfl))))).symm).trans (((h1 v0 (v1 ◇ (v2 ◇ v3)) ((v4 ◇ v2) ◇ v4) v1)).trans ((congrArg (fun q => q ◇ ((v4 ◇ v2) ◇ v4)) ((h1 v4 v2 v1 v3))).trans (congrArg (fun q => ((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ q) (rfl))))
have h10 (v0 v1 v2 v3 v4 : G) : ((((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) ◇ v2)) ◇ (v0 ◇ v1)) = (v0 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ v1)) ((congrArg (fun q => q ◇ ((v2 ◇ (((v0 ◇ v1) ◇ v0) ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3))) ◇ v2)) (rfl)).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ v2) ((congrArg (fun q => q ◇ (((v0 ◇ v1) ◇ v0) ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3))) (rfl)).trans (congrArg (fun q => v2 ◇ q) ((h1 v0 v1 v3 v4))))).trans (congrArg (fun q => (v2 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) ◇ q) (rfl)))))).trans (congrArg (fun q => (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) ◇ v2)) ◇ q) (rfl))).symm).trans (((h2 (v0 ◇ v1) v0 v2 ((v3 ◇ (v1 ◇ v4)) ◇ v3))).trans (rfl))
have h11 (v0 v1 v2 v3 : G) : (((v0 ◇ (v1 ◇ v2)) ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3))) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ ((((v3 ◇ v1) ◇ v3) ◇ ((v0 ◇ (v1 ◇ v2)) ◇ v0)) ◇ ((v3 ◇ v1) ◇ v3))) (rfl)).trans (congrArg (fun q => (v0 ◇ (v1 ◇ v2)) ◇ q) ((congrArg (fun q => q ◇ ((v3 ◇ v1) ◇ v3)) ((h1 v3 v1 v0 v2))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) (rfl)))))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3))) ◇ q) (rfl))).symm).trans (((h2 v0 (v1 ◇ v2) ((v3 ◇ v1) ◇ v3) v0)).trans (rfl))
have h12 (v0 v1 v2 v3 v4 v5 : G) : ((((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v4)) ◇ v3)) ◇ ((v5 ◇ v1) ◇ v5)) = ((v5 ◇ v1) ◇ v5) := by
  exact (((congrArg (fun q => q ◇ ((v5 ◇ v1) ◇ v5)) ((congrArg (fun q => q ◇ ((v3 ◇ ((((v5 ◇ v1) ◇ v5) ◇ ((v0 ◇ (v1 ◇ v2)) ◇ v0)) ◇ v4)) ◇ v3)) ((h1 v5 v1 v0 v2))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ ((((v5 ◇ v1) ◇ v5) ◇ ((v0 ◇ (v1 ◇ v2)) ◇ v0)) ◇ v4)) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((congrArg (fun q => q ◇ v4) ((h1 v5 v1 v0 v2))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) (rfl)))))).trans (congrArg (fun q => (v3 ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v4)) ◇ q) (rfl)))))).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ v4)) ◇ v3)) ◇ q) (rfl))).symm).trans (((h2 ((v5 ◇ v1) ◇ v5) ((v0 ◇ (v1 ◇ v2)) ◇ v0) v3 v4)).trans (rfl))
have h13 (v0 v1 v2 v3 v4 : G) : ((((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) ◇ ((v4 ◇ v1) ◇ v4)) = ((v4 ◇ v1) ◇ v4) := by
  exact (((congrArg (fun q => q ◇ ((v4 ◇ v1) ◇ v4)) ((congrArg (fun q => q ◇ ((v3 ◇ v1) ◇ v3)) ((h1 v3 v1 v0 v2))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) (rfl)))).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) ◇ q) (rfl))).symm).trans (((h7 ((v3 ◇ v1) ◇ v3) v0 v1 v2 v4)).trans (rfl))
have h14 (v0 v1 v2 v3 v4 v5 : G) : (((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v3 ◇ ((v4 ◇ (v0 ◇ v5)) ◇ v4)) ◇ v3)) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ ((v3 ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v4 ◇ (v0 ◇ v5)) ◇ v4))) ◇ v3)) (rfl)).trans (congrArg (fun q => (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ q) ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v4 ◇ (v0 ◇ v5)) ◇ v4))) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((h3 v0 v1 v2 v4 v5))))).trans (congrArg (fun q => (v3 ◇ ((v4 ◇ (v0 ◇ v5)) ◇ v4)) ◇ q) (rfl)))))).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v3 ◇ ((v4 ◇ (v0 ◇ v5)) ◇ v4)) ◇ v3)) ◇ q) (rfl))).symm).trans (((h2 v0 ((v1 ◇ (v0 ◇ v2)) ◇ v1) v3 ((v4 ◇ (v0 ◇ v5)) ◇ v4))).trans (rfl))
have h15 (v0 v1 v2 v3 v4 v5 : G) : ((((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ (v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3))) ◇ ((v5 ◇ v1) ◇ v5)) = ((v5 ◇ v1) ◇ v5) := by
  exact (((congrArg (fun q => q ◇ ((v5 ◇ v1) ◇ v5)) ((congrArg (fun q => q ◇ (v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3))) ((h3 v1 v3 v4 v0 v2))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) (rfl)))).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ (v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3))) ◇ q) (rfl))).symm).trans (((h7 (v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) v0 v1 v2 v5)).trans (rfl))
have h16 (v0 v1 v2 v3 v4 : G) : ((((v0 ◇ v1) ◇ v0) ◇ (((v2 ◇ (v1 ◇ v3)) ◇ v2) ◇ ((v4 ◇ v1) ◇ v4))) ◇ (v0 ◇ v1)) = (v0 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ v1)) ((congrArg (fun q => q ◇ ((((v4 ◇ v1) ◇ v4) ◇ ((v2 ◇ (v1 ◇ v3)) ◇ v2)) ◇ ((v4 ◇ v1) ◇ v4))) (rfl)).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ ((v4 ◇ v1) ◇ v4)) ((h1 v4 v1 v2 v3))).trans (congrArg (fun q => ((v2 ◇ (v1 ◇ v3)) ◇ v2) ◇ q) (rfl)))))).trans (congrArg (fun q => (((v0 ◇ v1) ◇ v0) ◇ (((v2 ◇ (v1 ◇ v3)) ◇ v2) ◇ ((v4 ◇ v1) ◇ v4))) ◇ q) (rfl))).symm).trans (((h10 v0 v1 ((v4 ◇ v1) ◇ v4) v2 v3)).trans (rfl))
have h17 (v0 v1 v2 v3 v4 v5 : G) : (((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ (((v3 ◇ (v0 ◇ v4)) ◇ v3) ◇ ((v5 ◇ v0) ◇ v5))) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ ((((v5 ◇ v0) ◇ v5) ◇ ((v3 ◇ (v0 ◇ v4)) ◇ v3)) ◇ ((v5 ◇ v0) ◇ v5))) (rfl)).trans (congrArg (fun q => (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ q) ((congrArg (fun q => q ◇ ((v5 ◇ v0) ◇ v5)) ((h1 v5 v0 v3 v4))).trans (congrArg (fun q => ((v3 ◇ (v0 ◇ v4)) ◇ v3) ◇ q) (rfl)))))).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ (((v3 ◇ (v0 ◇ v4)) ◇ v3) ◇ ((v5 ◇ v0) ◇ v5))) ◇ q) (rfl))).symm).trans (((h14 v0 v1 v2 ((v5 ◇ v0) ◇ v5) v3 v4)).trans (rfl))
have h18 (v0 v1 v2 v3 : G) : ((((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3)) ◇ (v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) = (v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) ((congrArg (fun q => q ◇ (((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ v0) ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3))) (rfl)).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ q) ((h8 v0 (v1 ◇ (v1 ◇ v2)) v1 v3 v1 v2))))).trans (congrArg (fun q => (((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3)) ◇ q) (rfl))).symm).trans (((h16 v0 ((v1 ◇ (v1 ◇ v2)) ◇ v1) v0 (v1 ◇ (v1 ◇ v2)) v3)).trans (rfl))
have h19 (v0 v1 v2 v3 : G) : (((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3)) = ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3)) ((h8 v0 (v1 ◇ (v1 ◇ v2)) v1 v0 v1 v2))).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h13 v0 ((v1 ◇ (v1 ◇ v2)) ◇ v1) (v1 ◇ (v1 ◇ v2)) v0 v3)).trans (rfl))
have h20 (v0 v1 v2 v3 : G) : (((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3)) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ (((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ v0) ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3))) (rfl)).trans (congrArg (fun q => (v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ q) ((h8 v0 (v1 ◇ (v1 ◇ v2)) v1 v3 v1 v2))))).trans (congrArg (fun q => ((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ ((v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v3)) ◇ q) (rfl))).symm).trans (((h11 v0 ((v1 ◇ (v1 ◇ v2)) ◇ v1) (v1 ◇ (v1 ◇ v2)) v3)).trans (rfl))
have h21 (v0 v1 v2 v3 : G) : (((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ (v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) = (v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) := by
  exact (((congrArg (fun q => q ◇ (v3 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) ((h19 v3 v1 v2 v0))).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h18 v3 v1 v2 v0)).trans (rfl))
have h22 (v0 v1 v2 v3 : G) : (((((((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)) ◇ ((v0 ◇ v1) ◇ v0)) ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ ((v2 ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ v2)) ◇ ((v3 ◇ (v0 ◇ v1)) ◇ v3)) = ((v3 ◇ (v0 ◇ v1)) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ (v0 ◇ v1)) ◇ v3)) ((congrArg (fun q => q ◇ ((v2 ◇ ((((((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)) ◇ ((v0 ◇ v1) ◇ v0)) ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)))) ◇ v2)) (rfl)).trans (congrArg (fun q => (((((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)) ◇ ((v0 ◇ v1) ◇ v0)) ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ q) ((congrArg (fun q => q ◇ v2) ((congrArg (fun q => q ◇ ((((((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)) ◇ ((v0 ◇ v1) ◇ v0)) ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)))) (rfl)).trans (congrArg (fun q => v2 ◇ q) ((h4 ((v0 ◇ v1) ◇ v0) v0 v1 (v0 ◇ v1)))))).trans (congrArg (fun q => (v2 ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ q) (rfl)))))).trans (congrArg (fun q => ((((((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)) ◇ ((v0 ◇ v1) ◇ v0)) ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ ((v2 ◇ (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1))) ◇ v2)) ◇ q) (rfl))).symm).trans (((h12 (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)) (v0 ◇ v1) v0 v2 (((v0 ◇ v1) ◇ v0) ◇ (v0 ◇ v1)) v3)).trans (rfl))
have h23 (v0 v1 v2 v3 v4 : G) : ((((((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0) ◇ (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1))) ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ ((v3 ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ v3)) ◇ ((v4 ◇ v0) ◇ v4)) = ((v4 ◇ v0) ◇ v4) := by
  exact (((congrArg (fun q => q ◇ ((v4 ◇ v0) ◇ v4)) ((congrArg (fun q => q ◇ ((v3 ◇ (((((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0) ◇ (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1))) ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0))) ◇ v3)) (rfl)).trans (congrArg (fun q => ((((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0) ◇ (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1))) ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ q) ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ (((((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0) ◇ (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1))) ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0))) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((h10 (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) v0 v0 v1 v2))))).trans (congrArg (fun q => (v3 ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ q) (rfl)))))).trans (congrArg (fun q => (((((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0) ◇ (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1))) ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ ((v3 ◇ ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0)) ◇ v3)) ◇ q) (rfl))).symm).trans (((h12 ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0) v0 ((v1 ◇ (v0 ◇ v2)) ◇ v1) v3 ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ v0) v4)).trans (rfl))
have h24 (v0 v1 v2 v3 : G) : (((v0 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v0) ◇ ((v3 ◇ (v1 ◇ v2)) ◇ v3)) = ((v3 ◇ (v1 ◇ v2)) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ (v1 ◇ v2)) ◇ v3)) ((h1 (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2)) ((v1 ◇ v2) ◇ v1) v0 (v1 ◇ v2)))).trans (congrArg (fun q => ((v0 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v0) ◇ q) (rfl))).symm).trans (((h22 v1 v2 v0 v3)).trans (rfl))
have h25 (v0 v1 v2 v3 v4 : G) : (((v0 ◇ ((v1 ◇ ((v2 ◇ (v1 ◇ v3)) ◇ v2)) ◇ v1)) ◇ v0) ◇ ((v4 ◇ v1) ◇ v4)) = ((v4 ◇ v1) ◇ v4) := by
  exact (((congrArg (fun q => q ◇ ((v4 ◇ v1) ◇ v4)) ((h1 ((v1 ◇ ((v2 ◇ (v1 ◇ v3)) ◇ v2)) ◇ v1) (v1 ◇ ((v2 ◇ (v1 ◇ v3)) ◇ v2)) v0 v1))).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ ((v2 ◇ (v1 ◇ v3)) ◇ v2)) ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h23 v1 v2 v3 v0 v4)).trans (rfl))
have h26 (v0 v1 v2 : G) : ((((v0 ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v0)) ◇ v0) ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v0)) ◇ ((v2 ◇ v0) ◇ v2)) = ((v2 ◇ v0) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ v0) ◇ v2)) ((congrArg (fun q => q ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v0)) ((h6 v0 v1 v0 v0))).trans (congrArg (fun q => ((v0 ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v0)) ◇ v0) ◇ q) (rfl)))).trans (congrArg (fun q => (((v0 ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v0)) ◇ v0) ◇ ((v0 ◇ (v0 ◇ v1)) ◇ v0)) ◇ q) (rfl))).symm).trans (((h25 ((v0 ◇ (v0 ◇ v1)) ◇ v0) v0 v0 v1 v2)).trans (rfl))
have h27 (v0 v1 v2 v3 v4 : G) : ((((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ ((v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) ◇ v1)) ◇ v2)) ◇ (v0 ◇ v1)) = (v0 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ v1)) ((congrArg (fun q => q ◇ ((v2 ◇ ((v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) ◇ v1)) ◇ v2)) ((h25 v2 v1 v3 v4 v0))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl)))).trans (congrArg (fun q => (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ ((v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) ◇ v1)) ◇ v2)) ◇ q) (rfl))).symm).trans (((h0 ((v2 ◇ ((v1 ◇ ((v3 ◇ (v1 ◇ v4)) ◇ v3)) ◇ v1)) ◇ v2) (v0 ◇ v1) v0)).trans (rfl))
have h28 (v0 v1 v2 v3 v4 v5 v6 : G) : ((((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ ((v4 ◇ v1) ◇ v4)) ◇ ((v5 ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6))) ◇ v5)) = ((v5 ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6))) ◇ v5) := by
  exact (((congrArg (fun q => q ◇ ((v5 ◇ (((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6)))) ◇ v5)) (rfl)).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ ((v4 ◇ v1) ◇ v4)) ◇ q) ((congrArg (fun q => q ◇ v5) ((congrArg (fun q => q ◇ (((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6)))) (rfl)).trans (congrArg (fun q => v5 ◇ q) ((h9 v0 v1 v2 v3 v6))))).trans (congrArg (fun q => (v5 ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6))) ◇ q) (rfl))))).symm).trans (((h5 v0 v1 (v2 ◇ v3) v4 v5 (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6)))).trans ((congrArg (fun q => q ◇ v5) ((congrArg (fun q => q ◇ (((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6)))) (rfl)).trans (congrArg (fun q => v5 ◇ q) ((h9 v0 v1 v2 v3 v6))))).trans (congrArg (fun q => (v5 ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6))) ◇ q) (rfl))))
have h29 (v0 v1 v2 v3 v4 : G) : ((((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v3)) ◇ ((v4 ◇ v1) ◇ v4)) = ((v4 ◇ v1) ◇ v4) := by
  exact (((congrArg (fun q => q ◇ ((v4 ◇ v1) ◇ v4)) ((congrArg (fun q => q ◇ ((v3 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v3)) ((h24 v3 v1 v2 v0))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) (rfl)))).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v3)) ◇ q) (rfl))).symm).trans (((h7 ((v3 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v3) v0 v1 v2 v4)).trans (rfl))
have h30 (v0 v1 v2 : G) : ((((v0 ◇ v1) ◇ v0) ◇ (((v1 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v1) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) ◇ (v0 ◇ v1)) = (v0 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ v1)) ((congrArg (fun q => q ◇ ((((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ ((v1 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v1)) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) (rfl)).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) ((congrArg (fun q => q ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ((h6 v1 v2 v1 v1))).trans (congrArg (fun q => ((v1 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v1) ◇ q) (rfl)))))).trans (congrArg (fun q => (((v0 ◇ v1) ◇ v0) ◇ (((v1 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v1) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) ◇ q) (rfl))).symm).trans (((h27 v0 v1 ((v1 ◇ (v1 ◇ v2)) ◇ v1) v1 v2)).trans (rfl))
have h31 (v0 v1 v2 v3 : G) : (((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ ((v3 ◇ v1) ◇ v3))) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ ((((v3 ◇ v1) ◇ v3) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ ((v3 ◇ v1) ◇ v3))) (rfl)).trans (congrArg (fun q => (v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ q) ((congrArg (fun q => q ◇ ((v3 ◇ v1) ◇ v3)) ((h1 v3 v1 v1 v2))).trans (congrArg (fun q => ((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ q) (rfl)))))).trans (congrArg (fun q => ((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ ((v3 ◇ v1) ◇ v3))) ◇ q) (rfl))).symm).trans (((h20 v0 v1 v2 ((v3 ◇ v1) ◇ v3))).trans (rfl))
have h32 (v0 v1 v2 : G) : (((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) = ((v1 ◇ (v1 ◇ v2)) ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (((v0 ◇ ((v0 ◇ ((v1 ◇ v2) ◇ v0)) ◇ v0)) ◇ v0) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) (rfl)).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v0) ◇ q) ((h7 v0 v0 (v1 ◇ v2) v0 v1)))).symm).trans (((h21 v0 v1 v2 ((v0 ◇ ((v0 ◇ ((v1 ◇ v2) ◇ v0)) ◇ v0)) ◇ v0))).trans ((h7 v0 v0 (v1 ◇ v2) v0 v1)))
have h33 (v0 v1 v2 v3 : G) : (((v0 ◇ v1) ◇ ((v2 ◇ (v2 ◇ v3)) ◇ v2)) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((h21 (v0 ◇ v1) v2 v3 (v0 ◇ v1)))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ ((v2 ◇ (v2 ◇ v3)) ◇ v2)) ◇ q) (rfl))).symm).trans (((h0 ((v0 ◇ v1) ◇ ((v2 ◇ (v2 ◇ v3)) ◇ v2)) v0 v1)).trans (rfl))
have h34 (v0 v1 v2 : G) : ((((v0 ◇ v1) ◇ v0) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ (v0 ◇ v1)) = (v0 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ v1)) ((congrArg (fun q => q ◇ (((v1 ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ v1) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1))) (rfl)).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) ((h32 v1 v1 v2))))).trans (congrArg (fun q => (((v0 ◇ v1) ◇ v0) ◇ ((v1 ◇ (v1 ◇ v2)) ◇ v1)) ◇ q) (rfl))).symm).trans (((h30 v0 v1 v2)).trans (rfl))
have h35 (v0 v1 v2 : G) : (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ ((v2 ◇ v0) ◇ v2)) = ((v2 ◇ v0) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ v0) ◇ v2)) ((h32 v0 v0 v1))).trans (congrArg (fun q => ((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h26 v0 v1 v2)).trans (rfl))
have h36 (v0 v1 v2 : G) : (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ (v2 ◇ v0)) = (v2 ◇ v0) := by
  exact (((congrArg (fun q => q ◇ (v2 ◇ v0)) ((h1 v2 v0 v0 v1))).trans (congrArg (fun q => ((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h34 v2 v0 v1)).trans (rfl))
have h37 (v0 v1 v2 v3 : G) : (((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ ((v3 ◇ v1) ◇ v3)) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ ((v3 ◇ v1) ◇ v3))) (rfl)).trans (congrArg (fun q => (v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ q) ((h35 v1 v2 v3))))).trans (congrArg (fun q => ((v0 ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) ◇ ((v3 ◇ v1) ◇ v3)) ◇ q) (rfl))).symm).trans (((h31 v0 v1 v2 v3)).trans (rfl))
have h38 (v0 v1 v2 : G) : (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ (v0 ◇ (v0 ◇ v2))) = (v0 ◇ (v0 ◇ v2)) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ (v0 ◇ v2))) ((h36 v0 v2 (v0 ◇ (v0 ◇ v1))))).trans (congrArg (fun q => ((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h33 (v0 ◇ (v0 ◇ v2)) v0 v0 v1)).trans (rfl))
have h39 (v0 v1 v2 v3 v4 : G) : ((((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ ((v2 ◇ v0) ◇ v2)) ◇ ((v3 ◇ (v4 ◇ v0)) ◇ v3)) = ((v3 ◇ (v4 ◇ v0)) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ (v4 ◇ v0))) ◇ v3)) (rfl)).trans (congrArg (fun q => (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ ((v2 ◇ v0) ◇ v2)) ◇ q) ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ (v4 ◇ v0))) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((h36 v0 v1 v4))))).trans (congrArg (fun q => (v3 ◇ (v4 ◇ v0)) ◇ q) (rfl))))).symm).trans (((h5 v0 v0 v1 v2 v3 (v4 ◇ v0))).trans ((congrArg (fun q => q ◇ v3) ((congrArg (fun q => q ◇ (((v0 ◇ (v0 ◇ v1)) ◇ v0) ◇ (v4 ◇ v0))) (rfl)).trans (congrArg (fun q => v3 ◇ q) ((h36 v0 v1 v4))))).trans (congrArg (fun q => (v3 ◇ (v4 ◇ v0)) ◇ q) (rfl))))
have h40 (v0 v1 v2 v3 : G) : (((v0 ◇ (v1 ◇ (v1 ◇ v2))) ◇ ((v3 ◇ v1) ◇ v3)) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ ((v3 ◇ v1) ◇ v3)) ((congrArg (fun q => q ◇ (((v1 ◇ (v1 ◇ v2)) ◇ v1) ◇ (v1 ◇ (v1 ◇ v2)))) (rfl)).trans (congrArg (fun q => v0 ◇ q) ((h38 v1 v2 v2))))).trans (congrArg (fun q => (v0 ◇ (v1 ◇ (v1 ◇ v2))) ◇ q) (rfl)))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ (v1 ◇ v2))) ◇ ((v3 ◇ v1) ◇ v3)) ◇ q) (rfl))).symm).trans (((h37 v0 v1 v2 v3)).trans (rfl))
have h41 (v0 v1 v2 v3 : G) : (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ (v3 ◇ v1)) ◇ v2)) = ((v2 ◇ (v3 ◇ v1)) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ (v3 ◇ v1)) ◇ v2)) ((h35 v1 v0 v0))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h39 v1 v0 v0 v2 v3)).trans (rfl))
have h42 (v0 v1 v2 v3 : G) : (((v0 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) = ((v3 ◇ v1) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ v1) ◇ v3)) ((h41 v0 (v1 ◇ v2) v0 ((v1 ◇ v2) ◇ v1)))).trans (congrArg (fun q => ((v0 ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) ◇ v0) ◇ q) (rfl))).symm).trans (((h29 v0 v1 v2 v0 v3)).trans (rfl))
have h43 (v0 v1 v2 : G) : (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ v1) ◇ v2)) = ((v2 ◇ v1) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ v1) ◇ v2)) ((h40 ((v0 ◇ v1) ◇ v0) v1 v0 v0))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h13 ((v0 ◇ v1) ◇ v0) v1 (v1 ◇ v0) v0 v2)).trans (rfl))
have h44 (v0 v1 v2 : G) : ((((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ v1) ◇ v2)) ◇ (v0 ◇ v1)) = (v0 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ v1)) ((congrArg (fun q => q ◇ (((((v2 ◇ v1) ◇ v2) ◇ (v1 ◇ (v1 ◇ v0))) ◇ ((v2 ◇ v1) ◇ v2)) ◇ ((v2 ◇ v1) ◇ v2))) (rfl)).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) ((h40 ((v2 ◇ v1) ◇ v2) v1 v0 v2))))).trans (congrArg (fun q => (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ v1) ◇ v2)) ◇ q) (rfl))).symm).trans (((h16 v0 v1 ((v2 ◇ v1) ◇ v2) (v1 ◇ v0) v2)).trans (rfl))
have h45 (v0 v1 v2 : G) : (((v0 ◇ v1) ◇ v0) ◇ (v2 ◇ v1)) = (v2 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v2 ◇ v1)) ((h43 v2 v1 v0))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h44 v2 v1 v0)).trans (rfl))
have h46 (v0 v1 v2 v3 : G) : (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v1) ◇ v3)) = ((v3 ◇ v1) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ v1) ◇ v3)) ((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ (((v1 ◇ v2) ◇ v1) ◇ (v1 ◇ v2))) (rfl)).trans (congrArg (fun q => v0 ◇ q) ((h45 v1 v2 v1))))).trans (congrArg (fun q => (v0 ◇ (v1 ◇ v2)) ◇ q) (rfl)))).trans (congrArg (fun q => ((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ q) (rfl))).symm).trans (((h42 v0 v1 v2 v3)).trans (rfl))
have h47 (v0 v1 v2 v3 : G) : (((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v3 ◇ v0) ◇ v3)) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((congrArg (fun q => q ◇ (((v0 ◇ (v0 ◇ v0)) ◇ v0) ◇ ((v3 ◇ v0) ◇ v3))) (rfl)).trans (congrArg (fun q => (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ q) ((h46 v0 v0 v0 v3))))).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v3 ◇ v0) ◇ v3)) ◇ q) (rfl))).symm).trans (((h17 v0 v1 v2 v0 v0 v3)).trans (rfl))
have h48 (v0 v1 v2 v3 v4 v5 v6 : G) : ((((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ ((v4 ◇ v1) ◇ v4)) ◇ ((v5 ◇ ((v6 ◇ v2) ◇ v6)) ◇ v5)) = ((v5 ◇ ((v6 ◇ v2) ◇ v6)) ◇ v5) := by
  exact (((congrArg (fun q => q ◇ ((v5 ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6))) ◇ v5)) (rfl)).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ (v2 ◇ v3))) ◇ v0) ◇ ((v4 ◇ v1) ◇ v4)) ◇ q) ((congrArg (fun q => q ◇ v5) ((congrArg (fun q => q ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6))) (rfl)).trans (congrArg (fun q => v5 ◇ q) ((h46 v1 v2 v3 v6))))).trans (congrArg (fun q => (v5 ◇ ((v6 ◇ v2) ◇ v6)) ◇ q) (rfl))))).symm).trans (((h28 v0 v1 v2 v3 v4 v5 v6)).trans ((congrArg (fun q => q ◇ v5) ((congrArg (fun q => q ◇ (((v1 ◇ (v2 ◇ v3)) ◇ v1) ◇ ((v6 ◇ v2) ◇ v6))) (rfl)).trans (congrArg (fun q => v5 ◇ q) ((h46 v1 v2 v3 v6))))).trans (congrArg (fun q => (v5 ◇ ((v6 ◇ v2) ◇ v6)) ◇ q) (rfl))))
have h49 (v0 v1 v2 v3 v4 : G) : (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ ((v3 ◇ v4) ◇ v3)) ◇ v2)) = ((v2 ◇ ((v3 ◇ v4) ◇ v3)) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ ((v3 ◇ v4) ◇ v3)) ◇ v2)) ((h46 v0 v1 (v4 ◇ v0) v0))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h48 v0 v1 v4 v0 v0 v2 v3)).trans (rfl))
have h50 (v0 v1 v2 v3 v4 : G) : (((v0 ◇ ((v1 ◇ (v2 ◇ v3)) ◇ v1)) ◇ v0) ◇ (v4 ◇ v2)) = (v4 ◇ v2) := by
  exact (((congrArg (fun q => q ◇ (v4 ◇ v2)) ((h49 v4 v2 v0 v1 (v2 ◇ v3)))).trans (congrArg (fun q => ((v0 ◇ ((v1 ◇ (v2 ◇ v3)) ◇ v1)) ◇ v0) ◇ q) (rfl))).symm).trans (((h10 v4 v2 v0 v1 v3)).trans (rfl))
have h51 (v0 v1 v2 : G) : (((v0 ◇ v1) ◇ v2) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((h45 (v0 ◇ v1) v2 (v0 ◇ v1)))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v2) ◇ q) (rfl))).symm).trans (((h0 ((v0 ◇ v1) ◇ v2) v0 v1)).trans (rfl))
have h52 (v0 v1 v2 v3 v4 : G) : ((((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v0) ◇ v3)) ◇ (v4 ◇ v1)) = (v4 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v4 ◇ v1)) ((h45 ((v0 ◇ (v1 ◇ v2)) ◇ v0) ((v3 ◇ v0) ◇ v3) ((v0 ◇ (v1 ◇ v2)) ◇ v0)))).trans (congrArg (fun q => (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v0) ◇ v3)) ◇ q) (rfl))).symm).trans (((h50 (((v0 ◇ (v1 ◇ v2)) ◇ v0) ◇ ((v3 ◇ v0) ◇ v3)) v0 v1 v2 v4)).trans (rfl))
have h53 (v0 v1 : G) : (v0 ◇ (v0 ◇ v1)) = (v0 ◇ v1) := by
  exact (((congrArg (fun q => q ◇ (v0 ◇ v1)) ((h2 v0 v1 v0 v0))).trans (congrArg (fun q => v0 ◇ q) (rfl))).symm).trans (((h51 (v0 ◇ v1) ((v0 ◇ ((v0 ◇ v1) ◇ v0)) ◇ v0) v0)).trans (rfl))
have h54 (v0 v1 v2 : G) : (((v0 ◇ v1) ◇ v0) ◇ ((v2 ◇ v0) ◇ v2)) = ((v2 ◇ v0) ◇ v2) := by
  exact (((congrArg (fun q => q ◇ ((v2 ◇ v0) ◇ v2)) ((congrArg (fun q => q ◇ v0) ((h53 v0 v1))).trans (congrArg (fun q => (v0 ◇ v1) ◇ q) (rfl)))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h35 v0 v1 v2)).trans (rfl))
have h55 (v0 v1 v2 v3 : G) : (((v0 ◇ v1) ◇ v0) ◇ (v2 ◇ v3)) = (v2 ◇ v3) := by
  exact (((congrArg (fun q => q ◇ (v2 ◇ v3)) ((h54 v1 (v3 ◇ v0) v0))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h52 v1 v3 v0 v0 v2)).trans (rfl))
have h56 (v0 v1 v2 v3 : G) : ((v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ ((v3 ◇ v0) ◇ v3)) = ((v3 ◇ v0) ◇ v3) := by
  exact (((congrArg (fun q => q ◇ ((v3 ◇ v0) ◇ v3)) ((h55 v0 (v0 ◇ v0) v0 ((v1 ◇ (v0 ◇ v2)) ◇ v1)))).trans (congrArg (fun q => (v0 ◇ ((v1 ◇ (v0 ◇ v2)) ◇ v1)) ◇ q) (rfl))).symm).trans (((h15 v0 v0 v0 v1 v2 v3)).trans (rfl))
have h57 (v0 v1 : G) : (((v0 ◇ v1) ◇ v0) ◇ v1) = v1 := by
  exact (((congrArg (fun q => q ◇ v1) ((h56 v1 v0 v0 v0))).trans (congrArg (fun q => ((v0 ◇ v1) ◇ v0) ◇ q) (rfl))).symm).trans (((h47 v1 v0 v0 v0)).trans (rfl))
have h58 (v0 v1 : G) : ((v0 ◇ v1) ◇ v0) = v0 := by
  exact (((congrArg (fun q => q ◇ v0) ((h45 v0 v1 v0))).trans (congrArg (fun q => (v0 ◇ v1) ◇ q) (rfl))).symm).trans (((h57 (v0 ◇ v1) v0)).trans (rfl))
have h59 (v0 v1 : G) : (v0 ◇ v1) = v1 := by
  exact (((congrArg (fun q => q ◇ v1) ((h58 v0 (v1 ◇ v0)))).trans (congrArg (fun q => v0 ◇ q) (rfl))).symm).trans (((h0 v0 v1 v0)).trans (rfl))
exact h59 y x"""

DISTILLED_LEFT_INSENSITIVE_LAW_PROOF = decompress(b85decode(
    "c-qZbOL7|_5Z(I}EQgJY&x}5<QmV4bITV-eNmVRIvN9$40y#qNmy-k-KzteoMoFBFMq;45dENbJT3>d@!wWj0H*~(~x5ESK32Fv{28srT?$9SJKIFi!pFhNt>L*jrfnbc$#*T~M=x&2PpKlO)IBoBbsOit&lq?~U;oH~q^Rre%9W?{DnnG1#71je>KZ$)Y>h{Oog^@K)bN{k?I($4lq2}@X4(-wAgZS{}v$Q-Ru{k_`#rXDk*zR5tBrdswy;z*npVK?7R-3Ps^hBX5;Z;VDz}wYo0%)cXBA;fW(y9H$fUvN>pxBQK>V<_ft<ED9L}uJnxg(5q7Md~U$OJHQnVJgY!3`cMFyzz4AjSd!BZEc^wkv5mKBxnN4vsVk1NCtr0SI0yw{=j+U*X23(8vsKLfDRJ?`gxe`p##Pp+!S?F{OY|+L&0(ln$H{a>C{^bEdkwyqMMn>zGcNYtWkDw@PaZBD!-Tnxab#v<cFqNz#K%5c1*7UlcJR0g`kBuzZ#d#zgfpk%1eN29X?HEi*<(9uZ$$Tb=hMN9?>9a79kLo;j{>M~u9bgeZ+A+)s1dwwi%kh?jg85#ADTqBZ>@Qw58*Z$00y#b&KQvsyD`OrfMAF-(czlne#6LXH%jb>T6eEfQE%Bsfvv!m!pNy_`))4yD&rOe}|jqy=U@60rd>Z?mU1Wn~q(pPC6m$Sm=z^xCBr$6_Qp#amHH-v~}G4VNi!CQrc<n@WmXU(P<>1{A{!Zy}^ygo2ahe*^8Bo6P?Lq~$n1J88iC=^wnm)@D}qMK%%ZJ@F4GbL)(Gi8(de%pkjVPr)r2G~D{St!_~;xJ6-noZ7|=U&8_m%cp#cLY`cz5s<nbI<>ZA2wZp4E)QaO5L$s0gD0Z@9yl89HIR;#U1WUgOvoRQi)&41b@yF?6`UZwJ8F?#mNe=@vZ2Y+Pa0rpF9DuQiy7cnwZMg!B%XO+b5VxY%Y820{#a!TDN!9#Ze@DT^O9i=1Cwg6^1y36=`|bCU_rPl4S7cXK`$lj-@ZfVWTKz*u6>fMZM9vIwQ`}oy@7P@vCio7L<^YaqQlq=MRBmR&fgio+!9DO(ATr2yNMa@pG8}mND?+Pi!+<c9rXc;ag4!^vZt>oQivZZpr-M^n?QC9q5g+QeZo9rz~kvt%e0Bp$7Vp?u^r63C2?QpW|SgLIH5Co`wdf9d7%"
)).decode("utf-8")


def _source_law_instance_proof(eq1_text, reference_text):
    """Prove a named source law directly from an alpha/symmetry instance."""
    return direct_substitution_proof(eq1_text, reference_text)


def _indent_local_proof(proof, spaces=2):
    prefix = " " * spaces
    return [prefix + line if line else "" for line in proof.splitlines()]


def _right_projection_reduction(term, theorem_name):
    if term[0] == VAR:
        return term, "rfl"
    leaf, right_proof = _right_projection_reduction(term[2], theorem_name)
    direct = "{} {} {}".format(
        theorem_name, render_term(term[1]), render_term(term[2])
    )
    if right_proof == "rfl":
        return leaf, direct
    return leaf, "({}).trans ({})".format(direct, right_proof)


def _left_insensitive_equality(left, right, theorem_name):
    if left == right:
        return "rfl"
    if left[0] != OP or right[0] != OP:
        return None
    right_proof = _left_insensitive_equality(left[2], right[2], theorem_name)
    if right_proof is None:
        return None
    ignore_left = "{} {} {} {}".format(
        theorem_name,
        render_term(left[1]),
        render_term(right[1]),
        render_term(left[2]),
    )
    if right_proof == "rfl":
        return ignore_left
    transport_right = "congrArg (fun q => {} ◇ q) ({})".format(
        render_term(right[1]), right_proof
    )
    return "({}).trans ({})".format(ignore_left, transport_right)


def _distilled_source_lines(name, reference_text, source_proof):
    lhs, rhs, variables = parse_equation(reference_text)
    lines = [
        "have {} : ∀ ({} : G), {} = {} := by".format(
            name,
            " ".join(variables),
            render_term(lhs),
            render_term(rhs),
        )
    ]
    lines.extend(_indent_local_proof(source_proof))
    return lines


DIRECT_COMMUTATIVITY_LAW = "x ◇ y = y ◇ x"
DIRECT_ASSOCIATIVITY_LAW = "(x ◇ y) ◇ z = x ◇ (y ◇ z)"


def _proof_trans(first, second):
    """Compose equality proofs while keeping generated certificates compact."""
    if first == "rfl":
        return second
    if second == "rfl":
        return first
    return "({}).trans ({})".format(first, second)


def _proof_symm(proof):
    if proof == "rfl":
        return proof
    return "({}).symm".format(proof)


def _binary_congruence(
    left,
    right,
    normalized_left,
    left_proof,
    right_proof,
):
    """Prove ``left ◇ right = normalized_left ◇ normalized_right``."""
    first = "rfl"
    if left_proof != "rfl":
        first = "congrArg (fun t => t ◇ {}) ({})".format(
            render_term(right), left_proof
        )
    second = "rfl"
    if right_proof != "rfl":
        second = "congrArg (fun t => {} ◇ t) ({})".format(
            render_term(normalized_left), right_proof
        )
    return _proof_trans(first, second)


def _direct_rewrite_application(h_variables, substitution, symmetric):
    if any(variable not in substitution for variable in h_variables):
        return None
    rendered = " ".join(
        render_term(substitution[variable]) for variable in h_variables
    )
    proof = "hyp" + ((" " + rendered) if rendered else "")
    if symmetric:
        proof = "({}).symm".format(proof)
    return proof


def _reducing_law_orientation(parsed_hypothesis):
    """Choose a fail-closed, size-decreasing orientation of the hypothesis."""
    left, right, h_variables = parsed_hypothesis
    candidates = (
        (left, right, False),
        (right, left, True),
    )
    for source, destination, symmetric in candidates:
        if source[0] == VAR:
            continue
        if not variables_set(destination).issubset(variables_set(source)):
            continue
        if term_size(source) <= term_size(destination):
            continue
        return source, destination, h_variables, symmetric
    return None


def _normalize_reducing_law(term, orientation, memo):
    """Bottom-up normalize with a universally quantified shrinking law."""
    cached = memo.get(term)
    if cached is not None:
        return cached
    if term[0] == VAR:
        result = (term, "rfl")
        memo[term] = result
        return result

    source, destination, h_variables, symmetric = orientation

    # Prefer a shrinking root rewrite before touching children.  This matters
    # for non-left-linear absorption laws: reducing one repeated branch first
    # can otherwise destroy an immediately available outer redex.
    substitution = {}
    if _match_pattern(source, term, substitution):
        application = _direct_rewrite_application(
            h_variables, substitution, symmetric
        )
        if application is not None:
            replacement = _instantiate(destination, substitution)
            if term_size(replacement) < term_size(term):
                normalized, tail = _normalize_reducing_law(
                    replacement, orientation, memo
                )
                result = (normalized, _proof_trans(application, tail))
                memo[term] = result
                return result

    left, left_proof = _normalize_reducing_law(term[1], orientation, memo)
    right, right_proof = _normalize_reducing_law(term[2], orientation, memo)
    current = (OP, left, right)
    proof = _binary_congruence(
        term[1], term[2], left, left_proof, right_proof
    )

    substitution = {}
    if _match_pattern(source, current, substitution):
        application = _direct_rewrite_application(
            h_variables, substitution, symmetric
        )
        if application is not None:
            replacement = _instantiate(destination, substitution)
            # Pattern size alone is insufficient when the smaller side repeats
            # a large variable.  Require every concrete rewrite to shrink.
            if term_size(replacement) < term_size(current):
                normalized, tail = _normalize_reducing_law(
                    replacement, orientation, memo
                )
                proof = _proof_trans(
                    proof, _proof_trans(application, tail)
                )
                result = (normalized, proof)
                memo[term] = result
                return result

    result = (current, proof)
    memo[term] = result
    return result


MAX_DIRECT_REDUCING_STATES = 256


def _reducing_rewrite_steps(term, orientation):
    """Yield every deterministic, concretely shrinking one-step rewrite."""
    source, destination, h_variables, symmetric = orientation
    seen = set()
    for path, subtree in _walk_paths(term):
        substitution = {}
        if not _match_pattern(source, subtree, substitution):
            continue
        application = _direct_rewrite_application(
            h_variables, substitution, symmetric
        )
        if application is None:
            continue
        replacement = _instantiate(destination, substitution)
        if term_size(replacement) >= term_size(subtree):
            continue
        next_term = _replace_at_path(term, path, replacement)
        if next_term in seen:
            continue
        seen.add(next_term)
        yield next_term, _wrap_congruence(term, path, application)


def _reducing_rewrite_closure(
    start, orientation, max_states=MAX_DIRECT_REDUCING_STATES
):
    """Return capped proofs from ``start`` to all shrinking descendants."""
    proofs = {start: "rfl"}
    depths = {start: 0}
    queue = deque([start])
    while queue and len(proofs) < max_states:
        current = queue.popleft()
        for next_term, edge_proof in _reducing_rewrite_steps(
            current, orientation
        ):
            if next_term in proofs:
                continue
            proofs[next_term] = _proof_trans(
                proofs[current], edge_proof
            )
            depths[next_term] = depths[current] + 1
            queue.append(next_term)
            if len(proofs) >= max_states:
                break
    return proofs, depths


def _reducing_common_descendant(goal_left, goal_right, orientation):
    """Meet two strictly decreasing rewrite closures, failing closed on caps."""
    left_proofs, left_depths = _reducing_rewrite_closure(
        goal_left, orientation
    )
    right_proofs, right_depths = _reducing_rewrite_closure(
        goal_right, orientation
    )
    common = set(left_proofs).intersection(right_proofs)
    if not common:
        return None
    meet = min(
        common,
        key=lambda term: (
            left_depths[term] + right_depths[term],
            term_size(term),
            repr(term),
        ),
    )
    return meet, left_proofs[meet], right_proofs[meet]


def _normalize_commutative(term, theorem_name, memo):
    cached = memo.get(term)
    if cached is not None:
        return cached
    if term[0] == VAR:
        result = (term, "rfl")
        memo[term] = result
        return result
    left, left_proof = _normalize_commutative(term[1], theorem_name, memo)
    right, right_proof = _normalize_commutative(term[2], theorem_name, memo)
    congruence = _binary_congruence(
        term[1], term[2], left, left_proof, right_proof
    )
    if repr(left) <= repr(right):
        result = ((OP, left, right), congruence)
    else:
        swap = "{} {} {}".format(
            theorem_name, render_term(left), render_term(right)
        )
        result = ((OP, right, left), _proof_trans(congruence, swap))
    memo[term] = result
    return result


def _fold_right_terms(terms):
    result = terms[-1]
    for term in reversed(terms[:-1]):
        result = (OP, term, result)
    return result


def _append_associative_factors(factors, right_term, theorem_name):
    """Right-associate ``foldr(factors) ◇ right_term`` with a proof."""
    if len(factors) == 1:
        return (OP, factors[0], right_term), "rfl"
    head = factors[0]
    rest = _fold_right_terms(factors[1:])
    target_tail, tail_proof = _append_associative_factors(
        factors[1:], right_term, theorem_name
    )
    step = "{} {} {} {}".format(
        theorem_name,
        render_term(head),
        render_term(rest),
        render_term(right_term),
    )
    if tail_proof != "rfl":
        wrapped = "congrArg (fun t => {} ◇ t) ({})".format(
            render_term(head), tail_proof
        )
        step = _proof_trans(step, wrapped)
    return (OP, head, target_tail), step


def _normalize_associative(term, theorem_name, memo):
    cached = memo.get(term)
    if cached is not None:
        return cached
    if term[0] == VAR:
        result = ((term,), term, "rfl")
        memo[term] = result
        return result

    left_factors, left, left_proof = _normalize_associative(
        term[1], theorem_name, memo
    )
    right_factors, right, right_proof = _normalize_associative(
        term[2], theorem_name, memo
    )
    congruence = _binary_congruence(
        term[1], term[2], left, left_proof, right_proof
    )
    normalized, append_proof = _append_associative_factors(
        list(left_factors), right, theorem_name
    )
    result = (
        left_factors + right_factors,
        normalized,
        _proof_trans(congruence, append_proof),
    )
    memo[term] = result
    return result


def _render_normalized_goal(goal_variables, left_proof, right_proof):
    lines = []
    intro = _intro_line(goal_variables)
    if intro:
        lines.append(intro)
    lines.append(
        "exact {}".format(
            _proof_trans(left_proof, _proof_symm(right_proof))
        )
    )
    return "\n".join(lines)


def direct_law_normalization_proof(eq1_text, eq2_text):
    """Normalize arbitrary goals under common direct equational laws.

    The first lane handles any concrete, strictly size-decreasing orientation
    of the supplied hypothesis.  Two specialized canonicalizers then cover
    direct commutativity and associativity, whose rules preserve term size.
    Every emitted step is reconstructed from ``hyp``, congruence, symmetry,
    and transitivity; no equation ID or answer table is consulted.
    """
    parsed_hypothesis = parse_equation(eq1_text)
    goal_left, goal_right, goal_variables = parse_equation(eq2_text)

    orientation = _reducing_law_orientation(parsed_hypothesis)
    if orientation is not None:
        left, left_proof = _normalize_reducing_law(
            goal_left, orientation, {}
        )
        right, right_proof = _normalize_reducing_law(
            goal_right, orientation, {}
        )
        if left == right:
            return _render_normalized_goal(
                goal_variables, left_proof, right_proof
            )
        meet = _reducing_common_descendant(
            goal_left, goal_right, orientation
        )
        if meet is not None:
            _, left_proof, right_proof = meet
            return _render_normalized_goal(
                goal_variables, left_proof, right_proof
            )

    source_proof = _source_law_instance_proof(
        eq1_text, DIRECT_COMMUTATIVITY_LAW
    )
    if source_proof is not None:
        left, left_proof = _normalize_commutative(
            goal_left, "commutative", {}
        )
        right, right_proof = _normalize_commutative(
            goal_right, "commutative", {}
        )
        if left == right:
            lines = _distilled_source_lines(
                "commutative",
                DIRECT_COMMUTATIVITY_LAW,
                source_proof,
            )
            lines.append(
                _render_normalized_goal(
                    goal_variables, left_proof, right_proof
                )
            )
            return "\n".join(lines)

    source_proof = _source_law_instance_proof(
        eq1_text, DIRECT_ASSOCIATIVITY_LAW
    )
    if source_proof is not None:
        _, left, left_proof = _normalize_associative(
            goal_left, "associative", {}
        )
        _, right, right_proof = _normalize_associative(
            goal_right, "associative", {}
        )
        if left == right:
            lines = _distilled_source_lines(
                "associative",
                DIRECT_ASSOCIATIVITY_LAW,
                source_proof,
            )
            lines.append(
                _render_normalized_goal(
                    goal_variables, left_proof, right_proof
                )
            )
            return "\n".join(lines)
    return None


def distilled_right_projection_proof(eq1_text, eq2_text):
    """Reduce both goal sides under a derived right-projection law."""
    source_proof = _source_law_instance_proof(
        eq1_text, DISTILLED_RIGHT_PROJECTION_SOURCE
    )
    if source_proof is None:
        return None
    goal_left, goal_right, goal_variables = parse_equation(eq2_text)
    left_leaf, left_proof = _right_projection_reduction(
        goal_left, "right_projection"
    )
    right_leaf, right_proof = _right_projection_reduction(
        goal_right, "right_projection"
    )
    if left_leaf != right_leaf:
        return None
    lines = _distilled_source_lines(
        "source_hyp",
        DISTILLED_RIGHT_PROJECTION_SOURCE,
        source_proof,
    )
    lines.append("have right_projection : ∀ a b : G, (a ◇ b) = b := by")
    lines.extend(
        _indent_local_proof(
            DISTILLED_RIGHT_PROJECTION_LAW_PROOF.replace(
                "hyp", "source_hyp"
            )
        )
    )
    intro = _intro_line(goal_variables)
    if intro:
        lines.append(intro)
    lines.append(
        "exact ({}).trans (({}).symm)".format(
            left_proof, right_proof
        )
    )
    return "\n".join(lines)


def _deduplicated_terms(terms, maximum_size=17):
    seen = set()
    result = []
    for term in terms:
        if term_size(term) > maximum_size or term in seen:
            continue
        seen.add(term)
        result.append(term)
    return result


def _rewrite_steps(
    root,
    eq1,
    term_pool,
    maximum_steps=320,
    maximum_choices=96,
    allow_variable_sides=False,
):
    rule_lhs, rule_rhs, h_variables = eq1
    # Variable-only sides generate an unhelpfully broad rewrite relation; the
    # stronger singleton/direct stages already cover their safe cheap cases.
    if not allow_variable_sides and (
        rule_lhs[0] == VAR or rule_rhs[0] == VAR
    ):
        return []

    results = []
    seen_roots = set()
    directions = (
        (rule_lhs, rule_rhs, False),
        (rule_rhs, rule_lhs, True),
    )
    for path, subtree in _walk_paths(root):
        for source, destination, symmetric in directions:
            base_substitution = {}
            if not _match_pattern(source, subtree, base_substitution):
                continue
            missing = [
                variable
                for variable in h_variables
                if variable not in base_substitution
            ]
            combinations = product(term_pool, repeat=len(missing))
            for choice_index, choices in enumerate(combinations):
                if choice_index >= maximum_choices:
                    break
                substitution = dict(base_substitution)
                substitution.update(zip(missing, choices))
                replacement = _instantiate(destination, substitution)
                next_root = _replace_at_path(root, path, replacement)
                if (
                    next_root == root
                    or term_size(next_root) > MAX_BIDIRECTIONAL_TERM_SIZE
                ):
                    continue
                if next_root in seen_roots:
                    continue
                arguments = " ".join(
                    render_term(substitution[variable]) for variable in h_variables
                )
                application = "hyp" + ((" " + arguments) if arguments else "")
                inner = "({})".format(application)
                if symmetric:
                    inner += ".symm"
                proof = _wrap_congruence(root, path, inner)
                seen_roots.add(next_root)
                results.append((next_root, proof))
                if len(results) >= maximum_steps:
                    return results
    return results


def _render_calc_chain(start, chain, goal_variables):
    lines = []
    intro = _intro_line(goal_variables)
    if intro:
        lines.append(intro)
    lines.append("calc")
    for index, (next_term, proof) in enumerate(chain):
        left = render_term(start) if index == 0 else "_"
        lines.append(
            "  {} = {} := {}".format(left, render_term(next_term), proof)
        )
    return "\n".join(lines)


def distilled_left_insensitive_proof(eq1_text, eq2_text):
    """Reduce equal right spines under the replayed left-insensitive law."""
    source_proof = _source_law_instance_proof(
        eq1_text, DISTILLED_LEFT_INSENSITIVE_SOURCE
    )
    if source_proof is None:
        return None
    goal_left, goal_right, goal_variables = parse_equation(eq2_text)
    proof = _left_insensitive_equality(
        goal_left, goal_right, "left_insensitive"
    )
    if proof is None:
        return None
    lines = _distilled_source_lines(
        "source_hyp", DISTILLED_LEFT_INSENSITIVE_SOURCE, source_proof
    )
    lines.append(
        "have left_insensitive : ∀ a b c : G, (a ◇ c) = (b ◇ c) := by"
    )
    lines.extend(
        _indent_local_proof(
            DISTILLED_LEFT_INSENSITIVE_LAW_PROOF.replace("hyp", "source_hyp")
        )
    )
    intro = _intro_line(goal_variables)
    if intro:
        lines.append(intro)
    lines.append("exact {}".format(proof))
    return "\n".join(lines)


def bounded_rewrite_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_REWRITE_DEPTH,
    max_states=MAX_REWRITE_STATES,
):
    """Find a deterministic bounded calc chain using instantiated ``h`` rewrites."""
    eq1 = parse_equation(eq1_text)
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if goal_lhs == goal_rhs:
        return reflexive_proof(eq2_text)

    static_terms = [(VAR, variable) for variable in goal_variables]
    static_terms.extend(iter_subterms(goal_lhs))
    static_terms.extend(iter_subterms(goal_rhs))
    term_pool = _deduplicated_terms(static_terms)

    queue = deque([(goal_lhs, [])])
    seen = {goal_lhs}
    while queue and len(seen) <= max_states:
        current, chain = queue.popleft()
        if len(chain) >= max_depth:
            continue
        dynamic_pool = _deduplicated_terms(
            term_pool + list(iter_subterms(current))
        )
        for next_term, proof in _rewrite_steps(current, eq1, dynamic_pool):
            if next_term in seen:
                continue
            next_chain = chain + [(next_term, proof)]
            if next_term == goal_rhs:
                return _render_calc_chain(goal_lhs, next_chain, goal_variables)
            seen.add(next_term)
            if len(seen) >= max_states:
                break
            queue.append((next_term, next_chain))
    return None


def _bounded_rewrite_closure(
    start,
    eq1,
    static_terms,
    max_depth,
    max_states,
    max_successors,
    max_choices,
):
    """Return deterministic rewrite predecessors from one side of a goal."""
    # term -> (parent term, proof of parent = term, depth)
    visited = {start: (None, None, 0)}
    queue = deque([start])
    while queue and len(visited) < max_states:
        current = queue.popleft()
        depth = visited[current][2]
        if depth >= max_depth:
            continue
        term_pool = _deduplicated_terms(
            static_terms + list(iter_subterms(current)),
            maximum_size=MAX_BIDIRECTIONAL_POOL_TERM_SIZE,
        )
        successors = _rewrite_steps(
            current,
            eq1,
            term_pool,
            maximum_steps=max_successors,
            maximum_choices=max_choices,
            allow_variable_sides=True,
        )
        for next_term, proof in successors:
            if next_term in visited:
                continue
            visited[next_term] = (current, proof, depth + 1)
            queue.append(next_term)
            if len(visited) >= max_states:
                break
    return visited


def _rewrite_edge_chain(visited, endpoint):
    """Recover (parent, child, parent=child proof) edges to ``endpoint``."""
    edges = []
    current = endpoint
    while True:
        parent, proof, _ = visited[current]
        if parent is None:
            break
        edges.append((parent, current, proof))
        current = parent
    edges.reverse()
    return edges


def bidirectional_bounded_rewrite_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_BIDIRECTIONAL_DEPTH,
    max_states=MAX_BIDIRECTIONAL_STATES,
    max_successors=MAX_BIDIRECTIONAL_SUCCESSORS,
    max_choices=MAX_BIDIRECTIONAL_CHOICES,
):
    """Meet-in-the-middle rewrite search with fixed, reproducible work caps."""
    eq1 = parse_equation(eq1_text)
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if goal_lhs == goal_rhs:
        return reflexive_proof(eq2_text)

    static_terms = [(VAR, variable) for variable in goal_variables]
    static_terms.extend(iter_subterms(goal_lhs))
    static_terms.extend(iter_subterms(goal_rhs))
    static_terms = _deduplicated_terms(
        static_terms,
        maximum_size=MAX_BIDIRECTIONAL_POOL_TERM_SIZE,
    )

    left = _bounded_rewrite_closure(
        goal_lhs,
        eq1,
        static_terms,
        max_depth,
        max_states,
        max_successors,
        max_choices,
    )
    right = _bounded_rewrite_closure(
        goal_rhs,
        eq1,
        static_terms,
        max_depth,
        max_states,
        max_successors,
        max_choices,
    )
    common = set(left).intersection(right)
    if not common:
        return None
    meet = min(
        common,
        key=lambda term: (
            left[term][2] + right[term][2],
            term_size(term),
            render_term(term),
        ),
    )

    left_edges = _rewrite_edge_chain(left, meet)
    right_edges = _rewrite_edge_chain(right, meet)
    chain = [(child, proof) for _, child, proof in left_edges]
    for parent, _, proof in reversed(right_edges):
        chain.append((parent, "({}).symm".format(proof)))
    if not chain or chain[-1][0] != goal_rhs:
        return None
    return _render_calc_chain(goal_lhs, chain, goal_variables)


def _symbolic_dereference(term, substitution):
    """Follow metavariable bindings without mutating ``substitution``."""
    seen = set()
    while term[0] == META and term in substitution and term not in seen:
        seen.add(term)
        term = substitution[term]
    return term


def _symbolic_resolve(term, substitution):
    term = _symbolic_dereference(term, substitution)
    if term[0] == OP:
        return (
            OP,
            _symbolic_resolve(term[1], substitution),
            _symbolic_resolve(term[2], substitution),
        )
    return term


def _symbolic_occurs(meta, term, substitution):
    term = _symbolic_dereference(term, substitution)
    if term == meta:
        return True
    return term[0] == OP and (
        _symbolic_occurs(meta, term[1], substitution)
        or _symbolic_occurs(meta, term[2], substitution)
    )


def _symbolic_unify(left, right, substitution):
    """First-order unification over rigid goal variables and ``META`` leaves."""
    left = _symbolic_dereference(left, substitution)
    right = _symbolic_dereference(right, substitution)
    if left == right:
        return True
    if left[0] == META:
        if _symbolic_occurs(left, right, substitution):
            return False
        substitution[left] = right
        return True
    if right[0] == META:
        if _symbolic_occurs(right, left, substitution):
            return False
        substitution[right] = left
        return True
    if left[0] != OP or right[0] != OP:
        return False
    return _symbolic_unify(left[1], right[1], substitution) and _symbolic_unify(
        left[2], right[2], substitution
    )


def _symbolic_rename(term, metas):
    if term[0] == VAR:
        return metas[term[1]]
    return (
        OP,
        _symbolic_rename(term[1], metas),
        _symbolic_rename(term[2], metas),
    )


def _symbolic_term_size(term):
    if term[0] != OP:
        return 1
    return 1 + _symbolic_term_size(term[1]) + _symbolic_term_size(term[2])


def _symbolic_canonical(term):
    """Alpha-normalize metavariables in preorder for deterministic deduplication."""
    names = {}

    def visit(node):
        if node[0] == META:
            if node not in names:
                names[node] = len(names)
            return (META, names[node])
        if node[0] == OP:
            return (OP, visit(node[1]), visit(node[2]))
        return node

    return visit(term)


def _symbolic_frontier(
    start,
    eq1,
    side,
    max_depth,
    max_states,
    max_term_size,
    max_successors,
):
    """Build a capped BFS of rewrite templates with symbolic substitutions."""
    rule_lhs, rule_rhs, h_variables = eq1
    # State: (term, substitution, edges, depth, serial).
    # Edge: (before, after, path, used_reverse_rule, application_meta_args).
    states = [(start, {}, (), 0, 0)]
    queue = deque([0])
    seen = {_symbolic_canonical(start)}
    directions = (
        (rule_lhs, rule_rhs, False),
        (rule_rhs, rule_lhs, True),
    )

    while queue and len(states) < max_states:
        term, substitution, edges, depth, serial = states[queue.popleft()]
        if depth >= max_depth:
            continue
        current = _symbolic_resolve(term, substitution)
        generated = 0
        for path_index, (path, subtree) in enumerate(_walk_paths(current)):
            for direction_index, (source, destination, symmetric) in enumerate(
                directions
            ):
                metas = {
                    variable: (
                        META,
                        side,
                        serial,
                        path_index,
                        direction_index,
                        variable,
                    )
                    for variable in h_variables
                }
                trial = dict(substitution)
                if not _symbolic_unify(
                    _symbolic_rename(source, metas), subtree, trial
                ):
                    continue
                before = _symbolic_resolve(term, trial)
                replacement = _symbolic_resolve(
                    _symbolic_rename(destination, metas), trial
                )
                after = _symbolic_resolve(
                    _replace_at_path(before, path, replacement), trial
                )
                if _symbolic_term_size(after) > max_term_size:
                    continue
                before_key = _symbolic_canonical(before)
                after_key = _symbolic_canonical(after)
                if after_key == before_key or after_key in seen:
                    continue

                seen.add(after_key)
                new_serial = len(states)
                edge = (
                    before,
                    after,
                    path,
                    symmetric,
                    tuple(metas[variable] for variable in h_variables),
                )
                states.append(
                    (
                        after,
                        trial,
                        edges + (edge,),
                        depth + 1,
                        new_serial,
                    )
                )
                generated += 1
                if len(states) >= max_states or generated >= max_successors:
                    break
                queue.append(new_serial)
            if len(states) >= max_states or generated >= max_successors:
                break
    return states


def _symbolic_ground(
    term,
    state_substitution,
    meet_substitution,
    fillers,
    filler,
):
    term = _symbolic_resolve(term, state_substitution)
    term = _symbolic_resolve(term, meet_substitution)
    if term[0] == META:
        if term not in fillers:
            fillers[term] = filler
        return fillers[term]
    if term[0] == OP:
        return (
            OP,
            _symbolic_ground(
                term[1],
                state_substitution,
                meet_substitution,
                fillers,
                filler,
            ),
            _symbolic_ground(
                term[2],
                state_substitution,
                meet_substitution,
                fillers,
                filler,
            ),
        )
    return term


def _symbolic_is_ground(term):
    if term[0] == META:
        return False
    return term[0] != OP or (
        _symbolic_is_ground(term[1]) and _symbolic_is_ground(term[2])
    )


def _subterm_at_path(term, path):
    for direction in path:
        if term[0] != OP:
            return None
        term = term[1] if direction == 0 else term[2]
    return term


def _symbolic_meet(left_states, right_states, goal_variables, max_depth):
    if not goal_variables:
        return None
    filler = (VAR, goal_variables[0])
    left_by_depth = [[] for _ in range(max_depth + 1)]
    right_by_depth = [[] for _ in range(max_depth + 1)]
    for state in left_states:
        left_by_depth[state[3]].append(state)
    for state in right_states:
        right_by_depth[state[3]].append(state)

    for total_depth in range(1, 2 * max_depth + 1):
        best = None
        best_key = None
        for left_depth in range(max_depth + 1):
            right_depth = total_depth - left_depth
            if right_depth < 0 or right_depth > max_depth:
                continue
            for left_state in left_by_depth[left_depth]:
                for right_state in right_by_depth[right_depth]:
                    meet_substitution = {}
                    left_term = _symbolic_resolve(
                        left_state[0], left_state[1]
                    )
                    right_term = _symbolic_resolve(
                        right_state[0], right_state[1]
                    )
                    if not _symbolic_unify(
                        left_term, right_term, meet_substitution
                    ):
                        continue
                    fillers = {}
                    meet = _symbolic_ground(
                        left_state[0],
                        left_state[1],
                        meet_substitution,
                        fillers,
                        filler,
                    )
                    if meet != _symbolic_ground(
                        right_state[0],
                        right_state[1],
                        meet_substitution,
                        fillers,
                        filler,
                    ):
                        continue
                    key = (
                        term_size(meet),
                        render_term(meet),
                        left_state[4],
                        right_state[4],
                    )
                    if best_key is None or key < best_key:
                        best_key = key
                        best = (left_state, right_state, meet_substitution)
        if best is not None:
            return best
    return None


def _symbolic_render_candidate(
    eq1,
    goal_lhs,
    goal_rhs,
    goal_variables,
    left_state,
    right_state,
    meet_substitution,
):
    if not goal_variables:
        return None
    rule_lhs, rule_rhs, h_variables = eq1
    filler = (VAR, goal_variables[0])
    fillers = {}

    def render_edge(edge, state_substitution):
        before_raw, after_raw, path, symmetric, raw_arguments = edge
        before = _symbolic_ground(
            before_raw,
            state_substitution,
            meet_substitution,
            fillers,
            filler,
        )
        after = _symbolic_ground(
            after_raw,
            state_substitution,
            meet_substitution,
            fillers,
            filler,
        )
        arguments = [
            _symbolic_ground(
                argument,
                state_substitution,
                meet_substitution,
                fillers,
                filler,
            )
            for argument in raw_arguments
        ]
        if not (
            _symbolic_is_ground(before)
            and _symbolic_is_ground(after)
            and all(_symbolic_is_ground(argument) for argument in arguments)
        ):
            return None

        source, destination = (
            (rule_rhs, rule_lhs) if symmetric else (rule_lhs, rule_rhs)
        )
        substitution = dict(zip(h_variables, arguments))
        if _instantiate(source, substitution) != _subterm_at_path(before, path):
            return None
        if _replace_at_path(
            before, path, _instantiate(destination, substitution)
        ) != after:
            return None

        rendered = " ".join(render_term(argument) for argument in arguments)
        application = "hyp" + ((" " + rendered) if rendered else "")
        inner = "({})".format(application)
        if symmetric:
            inner += ".symm"
        return before, after, _wrap_congruence(before, path, inner)

    left_rendered = []
    for edge in left_state[2]:
        rendered = render_edge(edge, left_state[1])
        if rendered is None:
            return None
        left_rendered.append(rendered)
    right_rendered = []
    for edge in right_state[2]:
        rendered = render_edge(edge, right_state[1])
        if rendered is None:
            return None
        right_rendered.append(rendered)

    left_meet = _symbolic_ground(
        left_state[0],
        left_state[1],
        meet_substitution,
        fillers,
        filler,
    )
    right_meet = _symbolic_ground(
        right_state[0],
        right_state[1],
        meet_substitution,
        fillers,
        filler,
    )
    if left_meet != right_meet:
        return None

    chain = []
    current = goal_lhs
    for before, after, proof in left_rendered:
        if before != current:
            return None
        chain.append((after, proof))
        current = after
    if current != left_meet:
        return None

    right_current = goal_rhs
    for before, after, _ in right_rendered:
        if before != right_current:
            return None
        right_current = after
    if right_current != right_meet:
        return None
    for before, after, proof in reversed(right_rendered):
        if after != current:
            return None
        chain.append((before, "({}).symm".format(proof)))
        current = before
    if current != goal_rhs or not chain:
        return None
    return _render_calc_chain(goal_lhs, chain, goal_variables)


def _symbolic_narrowing_at_depth(
    eq1,
    goal_lhs,
    goal_rhs,
    goal_variables,
    max_depth,
    max_states,
    max_term_size,
    max_successors,
):
    left_states = _symbolic_frontier(
        goal_lhs,
        eq1,
        "left",
        max_depth,
        max_states,
        max_term_size,
        max_successors,
    )
    right_states = _symbolic_frontier(
        goal_rhs,
        eq1,
        "right",
        max_depth,
        max_states,
        max_term_size,
        max_successors,
    )
    meet = _symbolic_meet(
        left_states, right_states, goal_variables, max_depth
    )
    if meet is None:
        return None
    return _symbolic_render_candidate(
        eq1,
        goal_lhs,
        goal_rhs,
        goal_variables,
        meet[0],
        meet[1],
        meet[2],
    )


def symbolic_narrowing_proof(
    eq1_text,
    eq2_text,
    max_states=MAX_SYMBOLIC_STATES,
    max_term_size=MAX_SYMBOLIC_TERM_SIZE,
    max_successors=MAX_SYMBOLIC_SUCCESSORS,
):
    """Find a grounded proof by deterministic symbolic narrowing, D2 then D3."""
    eq1 = parse_equation(eq1_text)
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if goal_lhs == goal_rhs:
        return reflexive_proof(eq2_text)
    for max_depth in (2, 3):
        proof = _symbolic_narrowing_at_depth(
            eq1,
            goal_lhs,
            goal_rhs,
            goal_variables,
            max_depth,
            max_states,
            max_term_size,
            max_successors,
        )
        if proof is not None:
            return proof
    return None


def _symbolic_structural_mismatch(left, right):
    """A deterministic lower-is-better shape distance for beam ordering."""
    if left[0] == META or right[0] == META:
        return 0
    if left[0] == OP and right[0] == OP:
        return _symbolic_structural_mismatch(
            left[1], right[1]
        ) + _symbolic_structural_mismatch(left[2], right[2])
    if left[0] == OP or right[0] == OP:
        return 2 + abs(
            _symbolic_term_size(left) - _symbolic_term_size(right)
        )
    return 0 if left == right else 1


def _symbolic_beam_score(term, target, generation_ordinal):
    trial = {}
    if _symbolic_unify(term, target, trial):
        conflict = 0
    else:
        conflict = 1 + _symbolic_structural_mismatch(term, target)
    size = _symbolic_term_size(term)
    return (
        conflict,
        abs(size - _symbolic_term_size(target)),
        size,
        str(_symbolic_canonical(term)),
        generation_ordinal,
    )


def _symbolic_beam_frontier(start, target, eq1, side):
    return {
        "target": target,
        "eq1": eq1,
        "side": side,
        "states": [(start, {}, (), 0, 0)],
        "layer": [0],
        # Generated forms are marked before pruning.  A later path cannot
        # reintroduce a shape that lost the deterministic beam tie-break.
        "seen": {_symbolic_canonical(start)},
    }


def _symbolic_beam_extend(
    frontier,
    depth,
    beam_width,
    max_term_size,
    max_successors,
):
    rule_lhs, rule_rhs, h_variables = frontier["eq1"]
    directions = (
        (rule_lhs, rule_rhs, False),
        (rule_rhs, rule_lhs, True),
    )
    candidates = []
    for state_index in frontier["layer"]:
        term, substitution, edges, _, serial = frontier["states"][state_index]
        current = _symbolic_resolve(term, substitution)
        generated = 0
        for path_index, (path, subtree) in enumerate(_walk_paths(current)):
            for direction_index, (source, destination, symmetric) in enumerate(
                directions
            ):
                metas = {
                    variable: (
                        META,
                        frontier["side"],
                        serial,
                        path_index,
                        direction_index,
                        variable,
                    )
                    for variable in h_variables
                }
                trial = dict(substitution)
                if not _symbolic_unify(
                    _symbolic_rename(source, metas), subtree, trial
                ):
                    continue
                before = _symbolic_resolve(term, trial)
                replacement = _symbolic_resolve(
                    _symbolic_rename(destination, metas), trial
                )
                after = _symbolic_resolve(
                    _replace_at_path(before, path, replacement), trial
                )
                after_key = _symbolic_canonical(after)
                if (
                    _symbolic_term_size(after) > max_term_size
                    or after_key == _symbolic_canonical(before)
                    or after_key in frontier["seen"]
                ):
                    continue

                frontier["seen"].add(after_key)
                edge = (
                    before,
                    after,
                    path,
                    symmetric,
                    tuple(metas[variable] for variable in h_variables),
                )
                candidates.append(
                    (
                        after,
                        trial,
                        edges + (edge,),
                        depth,
                        len(candidates),
                    )
                )
                generated += 1
                if generated >= max_successors:
                    break
            if generated >= max_successors:
                break

    candidates.sort(
        key=lambda state: _symbolic_beam_score(
            _symbolic_resolve(state[0], state[1]),
            frontier["target"],
            state[4],
        )
    )
    frontier["layer"] = []
    for term, substitution, edges, state_depth, _ in candidates[:beam_width]:
        serial = len(frontier["states"])
        frontier["states"].append(
            (term, substitution, edges, state_depth, serial)
        )
        frontier["layer"].append(serial)
    return bool(frontier["layer"])


def goal_guided_symbolic_beam_proof(
    eq1_text,
    eq2_text,
    max_depth=MAX_SYMBOLIC_BEAM_DEPTH,
    beam_width=MAX_SYMBOLIC_BEAM_WIDTH,
    max_term_size=MAX_SYMBOLIC_BEAM_TERM_SIZE,
    max_successors=MAX_SYMBOLIC_BEAM_SUCCESSORS,
):
    """Search deeper symbolic paths with a fixed, goal-guided beam."""
    eq1 = parse_equation(eq1_text)
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if goal_lhs == goal_rhs:
        return reflexive_proof(eq2_text)

    left = _symbolic_beam_frontier(
        goal_lhs, goal_rhs, eq1, "beam-left"
    )
    right = _symbolic_beam_frontier(
        goal_rhs, goal_lhs, eq1, "beam-right"
    )
    for depth in range(1, max_depth + 1):
        left_alive = _symbolic_beam_extend(
            left,
            depth,
            beam_width,
            max_term_size,
            max_successors,
        )
        right_alive = _symbolic_beam_extend(
            right,
            depth,
            beam_width,
            max_term_size,
            max_successors,
        )
        meet = _symbolic_meet(
            left["states"], right["states"], goal_variables, depth
        )
        if meet is not None:
            proof = _symbolic_render_candidate(
                eq1,
                goal_lhs,
                goal_rhs,
                goal_variables,
                meet[0],
                meet[1],
                meet[2],
            )
            if proof is not None:
                return proof
        if not left_alive and not right_alive:
            break
    return None


def _retained_symbolic_beam_extend(
    frontier,
    depth,
    beam_width,
    max_term_size,
    max_successors,
):
    """Extend a beam without letting discarded paths poison future deduplication."""
    rule_lhs, rule_rhs, h_variables = frontier["eq1"]
    directions = (
        (rule_lhs, rule_rhs, False),
        (rule_rhs, rule_lhs, True),
    )
    layer_best = {}
    generation_ordinal = 0
    for state_index in frontier["layer"]:
        term, substitution, edges, _, serial = frontier["states"][state_index]
        current = _symbolic_resolve(term, substitution)
        generated = 0
        for path_index, (path, subtree) in enumerate(_walk_paths(current)):
            for direction_index, (source, destination, symmetric) in enumerate(
                directions
            ):
                metas = {
                    variable: (
                        META,
                        frontier["side"],
                        serial,
                        path_index,
                        direction_index,
                        variable,
                    )
                    for variable in h_variables
                }
                trial = dict(substitution)
                if not _symbolic_unify(
                    _symbolic_rename(source, metas), subtree, trial
                ):
                    continue
                before = _symbolic_resolve(term, trial)
                replacement = _symbolic_resolve(
                    _symbolic_rename(destination, metas), trial
                )
                after = _symbolic_resolve(
                    _replace_at_path(before, path, replacement), trial
                )
                after_key = _symbolic_canonical(after)
                if (
                    _symbolic_term_size(after) > max_term_size
                    or after_key == _symbolic_canonical(before)
                    or after_key in frontier["seen"]
                ):
                    continue

                edge = (
                    before,
                    after,
                    path,
                    symmetric,
                    tuple(metas[variable] for variable in h_variables),
                )
                state = (
                    after,
                    trial,
                    edges + (edge,),
                    depth,
                    generation_ordinal,
                )
                score = _symbolic_beam_score(
                    _symbolic_resolve(after, trial),
                    frontier["target"],
                    generation_ordinal,
                )
                previous = layer_best.get(after_key)
                if previous is None or score < previous[0]:
                    layer_best[after_key] = (score, state)
                generation_ordinal += 1
                generated += 1
                if generated >= max_successors:
                    break
            if generated >= max_successors:
                break

    candidates = [entry[1] for entry in layer_best.values()]
    candidates.sort(
        key=lambda state: _symbolic_beam_score(
            _symbolic_resolve(state[0], state[1]),
            frontier["target"],
            state[4],
        )
    )
    frontier["layer"] = []
    for term, substitution, edges, state_depth, _ in candidates[:beam_width]:
        frontier["seen"].add(
            _symbolic_canonical(_symbolic_resolve(term, substitution))
        )
        serial = len(frontier["states"])
        frontier["states"].append(
            (term, substitution, edges, state_depth, serial)
        )
        frontier["layer"].append(serial)
    return bool(frontier["layer"])

def _symbolic_pair_meet(left_state, right_state, goal_variables):
    if not goal_variables:
        return None
    filler = (VAR, goal_variables[0])
    meet_substitution = {}
    left_term = _symbolic_resolve(left_state[0], left_state[1])
    right_term = _symbolic_resolve(right_state[0], right_state[1])
    if not _symbolic_unify(left_term, right_term, meet_substitution):
        return None
    fillers = {}
    left_meet = _symbolic_ground(
        left_state[0],
        left_state[1],
        meet_substitution,
        fillers,
        filler,
    )
    right_meet = _symbolic_ground(
        right_state[0],
        right_state[1],
        meet_substitution,
        fillers,
        filler,
    )
    if left_meet != right_meet:
        return None
    return left_state, right_state, meet_substitution

def _incremental_symbolic_meets(
    left,
    right,
    new_left,
    new_right,
    goal_variables,
):
    """Yield new cross-frontier meets in deterministic shallow-first order."""
    pairs = []
    for left_index in new_left:
        left_state = left["states"][left_index]
        for right_index, right_state in enumerate(right["states"]):
            pairs.append(
                (
                    left_state[3] + right_state[3],
                    left_index,
                    right_index,
                )
            )
    old_left_end = new_left[0] if new_left else len(left["states"])
    for right_index in new_right:
        right_state = right["states"][right_index]
        for left_index in range(old_left_end):
            left_state = left["states"][left_index]
            pairs.append(
                (
                    left_state[3] + right_state[3],
                    left_index,
                    right_index,
                )
            )
    pairs.sort()
    for _, left_index, right_index in pairs:
        meet = _symbolic_pair_meet(
            left["states"][left_index],
            right["states"][right_index],
            goal_variables,
        )
        if meet is not None:
            yield meet

def deep_goal_guided_symbolic_beam_proof(
    eq1_text,
    eq2_text,
    tiers=DEEP_SYMBOLIC_BEAM_TIERS,
):
    """Try a fast retained beam, then a broader fixed fallback tier."""
    eq1 = parse_equation(eq1_text)
    goal_lhs, goal_rhs, goal_variables = parse_equation(eq2_text)
    if goal_lhs == goal_rhs:
        return reflexive_proof(eq2_text)

    for max_depth, beam_width, max_term_size, max_successors in tiers:
        left = _symbolic_beam_frontier(
            goal_lhs, goal_rhs, eq1, "deep-beam-left"
        )
        right = _symbolic_beam_frontier(
            goal_rhs, goal_lhs, eq1, "deep-beam-right"
        )
        for depth in range(1, max_depth + 1):
            left_alive = _retained_symbolic_beam_extend(
                left, depth, beam_width, max_term_size, max_successors
            )
            new_left = list(left["layer"])
            right_alive = _retained_symbolic_beam_extend(
                right, depth, beam_width, max_term_size, max_successors
            )
            new_right = list(right["layer"])
            for meet in _incremental_symbolic_meets(
                left, right, new_left, new_right, goal_variables
            ):
                proof = _symbolic_render_candidate(
                    eq1,
                    goal_lhs,
                    goal_rhs,
                    goal_variables,
                    meet[0],
                    meet[1],
                    meet[2],
                )
                if proof is not None:
                    return proof
            if not left_alive and not right_alive:
                break
    return None

def make_true_code(proof_body):
    lines = proof_body.strip().splitlines()
    nonempty = [line for line in lines if line.strip()]
    if nonempty:
        indent = min(len(line) - len(line.lstrip()) for line in nonempty)
        lines = [line[indent:] if line.strip() else "" for line in lines]
    indented = "\n".join("  " + line if line.strip() else "" for line in lines)
    return (
        "import JudgeProblem\n\n"
        "def submission : Goal := by\n"
        "  intro G _ hyp\n"
        + indented
        + "\n"
    )


def _counterexample_witness(parsed_equation, n, table):
    """Return the first deterministic assignment that refutes an equation."""
    lhs, rhs, variables = parsed_equation
    for values in product(range(n), repeat=len(variables)):
        environment = dict(zip(variables, values))
        if evaluate_term(lhs, environment, table) != evaluate_term(
            rhs, environment, table
        ):
            return values
    return None


def _make_structural_false_code(n, table, eq1_text, eq2_text):
    """Build an axiom-free finite certificate by exhaustive constructor cases.

    Larger carriers cannot use the official digit-oriented ``finOpTable``
    decoder.  A custom inductive carrier makes every operation-table entry a
    kernel reduction.  The hypothesis is checked by exhaustive ``cases`` and a
    concrete constructor inequality refutes the goal.  The fixed case and byte
    caps make this lane fail closed before an expensive certificate is emitted.
    """
    if not isinstance(eq1_text, str) or not isinstance(eq2_text, str):
        return None
    parsed_hypothesis = parse_equation(eq1_text)
    parsed_goal = parse_equation(eq2_text)
    hypothesis_variables = parsed_hypothesis[2]
    if n ** len(hypothesis_variables) > MAX_STRUCTURAL_COUNTERMODEL_CASES:
        return None
    if not equation_holds(parsed_hypothesis, n, table):
        return None
    witness = _counterexample_witness(parsed_goal, n, table)
    if witness is None:
        return None

    lines = ["import JudgeProblem", "", "namespace submission", "", "inductive Carrier where"]
    lines.extend("  | c{}".format(index) for index in range(n))
    lines.extend(
        [
            "",
            "@[reducible] def candidateOp : Carrier → Carrier → Carrier",
        ]
    )
    for row_index, row in enumerate(table):
        for column_index, value in enumerate(row):
            lines.append(
                "  | .c{}, .c{} => .c{}".format(
                    row_index, column_index, value
                )
            )
    lines.extend(
        [
            "",
            "@[reducible] def candidateMagma : Magma Carrier := {",
            "  op := candidateOp",
            "}",
            "",
            "def proof : Goal := by",
            "  refine ⟨Carrier, candidateMagma, ?_, ?_⟩",
        ]
    )
    if hypothesis_variables:
        lines.append("  · intro {}".format(" ".join(hypothesis_variables)))
        lines.append(
            "    {} <;> rfl".format(
                " <;> ".join(
                    "cases {}".format(variable)
                    for variable in hypothesis_variables
                )
            )
        )
    else:
        lines.append("  · rfl")
    lines.append("  · intro h")
    witness_arguments = " ".join(
        ".c{}".format(value) for value in witness
    )
    lines.append(
        "    have bad := h{}".format(
            (" " + witness_arguments) if witness_arguments else ""
        )
    )
    lines.append("    cases bad")
    lines.extend(
        [
            "",
            "end submission",
            "",
            "def submission : Goal := submission.proof",
        ]
    )
    code = "\n".join(lines) + "\n"
    if len(code.encode("utf-8")) > MAX_STRUCTURAL_FALSE_CERT_BYTES:
        return None
    return code


def make_false_code(n, table, eq1_text=None, eq2_text=None):
    actual_n = validate_table(table)
    if actual_n != n:
        raise ValueError("counterexample carrier does not match its table")
    if n > MAX_LLM_COUNTERMODEL_CARRIER:
        return _make_structural_false_code(
            n, table, eq1_text, eq2_text
        )
    table_text = json.dumps(table, separators=(",", ":"))
    return (
        "import JudgeProblem\n"
        "import JudgeDecide.DecideBang\n"
        "import JudgeFinOp.MemoFinOp\n"
        "open MemoFinOp\n\n"
        "set_option maxRecDepth 100000 in\n"
        "def submission : Goal := by\n"
        "  let candidateMagma : Magma (Fin {n}) := {{\n"
        "    op := finOpTable \"{table}\"\n"
        "  }}\n"
        "  refine ⟨Fin {n}, candidateMagma, ?_⟩\n"
        "  decideFin!\n"
    ).format(n=n, table=table_text)


def extract_json(text):
    if not isinstance(text, str):
        return None
    cleaned = re.sub(r"<think>[\s\S]*?</think>", "", text).strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        value = json.loads(cleaned)
        return value if isinstance(value, dict) else None
    except (TypeError, ValueError):
        pass
    match = re.search(r"\{[\s\S]*\}", cleaned)
    if match:
        try:
            value = json.loads(match.group(0))
            return value if isinstance(value, dict) else None
        except (TypeError, ValueError):
            return None
    return None


def clean_proof_body(proof):
    if not isinstance(proof, str):
        return ""
    proof = normalize_operator(proof).strip()
    proof = re.sub(r"^```(?:lean)?\s*", "", proof, flags=re.IGNORECASE)
    proof = re.sub(r"\s*```$", "", proof)
    header = re.match(
        r"^\s*(?:def|theorem)\s+submission[\s\S]*?:=\s*by\s*",
        proof,
    )
    if header:
        proof = proof[header.end() :]
    proof = re.sub(r"^\s*by\s+", "", proof, count=1)
    proof = re.sub(r"^\s*import\s+[^\n]*\n?", "", proof, flags=re.MULTILINE)
    return proof.strip()


def read_message():
    line = sys.stdin.readline()
    if not line:
        raise EOFError("proxy closed stdin")
    return json.loads(line)


def send_message(message):
    print(json.dumps(message, separators=(",", ":")), flush=True)


def call_judge(verdict, code):
    send_message({"call": "judge", "verdict": verdict, "code": code})
    return read_message()


def call_llm(context):
    # The organizer proxy owns routing, credentials, and any model billing.
    # This solver intentionally has no direct API path.
    send_message({"call": "llm", "context": context})
    return read_message()


def log_event(event, **fields):
    payload = {"event": event}
    payload.update(fields)
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")), file=sys.stderr)


def _feedback_text(response, maximum=900):
    if not isinstance(response, dict):
        return "invalid judge response"
    detail = response.get("stderr") or response.get("message") or ""
    detail = re.sub(r"\s+", " ", str(detail)).strip()
    if len(detail) > maximum:
        detail = detail[:maximum] + "..."
    status = str(response.get("status", "unknown"))
    return "{}: {}".format(status, detail) if detail else status


def _judge_candidate(strategy, verdict, code, trace, feedback):
    log_event("candidate", strategy=strategy, verdict=verdict, code_bytes=len(code.encode("utf-8")))
    response = call_judge(verdict, code)
    summary = _feedback_text(response)
    trace.append("{} -> {}".format(strategy, summary))
    feedback.append(summary)
    log_event("judge_result", strategy=strategy, status=response.get("status", "unknown"))
    return response.get("status") == "accepted"


def _llm_fallback(problem, eq1_text, eq2_text, trace, feedback):
    seen = set()
    for round_number in range(MAX_LLM_ROUNDS):
        context = {
            "round": str(round_number),
            "deterministic_trace": "\n".join(trace),
            "last_feedback": feedback[-1] if feedback else "none",
        }
        log_event("llm_request", round=round_number, route="organizer_proxy")
        response = call_llm(context)
        if not isinstance(response, dict) or "error" in response:
            log_event("llm_unavailable", round=round_number)
            return False
        answer = extract_json(response.get("response", ""))
        if not answer:
            trace.append("llm round {} -> unparseable JSON".format(round_number))
            continue
        verdict = answer.get("verdict")
        if verdict == "true":
            proof = clean_proof_body(answer.get("proof", ""))
            if not proof or proof in seen:
                continue
            seen.add(proof)
            code = make_true_code(proof)
        elif verdict == "false":
            table = answer.get("counterexample_table")
            n = validate_table(
                table, maximum=MAX_LLM_COUNTERMODEL_CARRIER
            )
            if n is None:
                trace.append("llm round {} -> invalid table shape".format(round_number))
                continue
            key = json.dumps(table, separators=(",", ":"))
            if key in seen:
                continue
            seen.add(key)
            satisfies_hypothesis, satisfies_goal = verify_counterexample(
                eq1_text, eq2_text, table
            )
            if not satisfies_hypothesis or satisfies_goal:
                trace.append("llm round {} -> table rejected locally".format(round_number))
                continue
            code = make_false_code(n, table, eq1_text, eq2_text)
        else:
            continue
        if _judge_candidate(
            "organizer_proxy_llm_round_{}".format(round_number),
            verdict,
            code,
            trace,
            feedback,
        ):
            return True
    return False


def main():
    startup = read_message()
    problem = startup["problem"]
    eq1_text = normalize_operator(problem["equation1"])
    eq2_text = normalize_operator(problem["equation2"])
    problem["equation1"] = eq1_text
    problem["equation2"] = eq2_text

    trace = [
        "strategy order: {}".format(" -> ".join(STRATEGY_ORDER)),
        "canonical hypothesis: {}".format(canonical_equation_text(eq1_text)),
        "canonical goal: {}".format(canonical_equation_text(eq2_text)),
    ]
    feedback = []
    tried_code = set()

    quick_strategies = (
        ("reflexive_goal", lambda: reflexive_proof(eq2_text)),
        (
            "direct_substitution",
            lambda: direct_substitution_proof(eq1_text, eq2_text),
        ),
        (
            "singleton_collapse",
            lambda: singleton_collapse_proof(eq1_text, eq2_text),
        ),
        (
            "singleton_forcing_source_paramodulation",
            lambda: singleton_forcing_source_proof(eq1_text, eq2_text),
        ),
    )
    for strategy, build_proof in quick_strategies:
        proof = build_proof()
        if not proof:
            trace.append("{} -> no candidate".format(strategy))
            continue
        code = make_true_code(proof)
        if code in tried_code:
            trace.append("{} -> duplicate candidate".format(strategy))
            continue
        tried_code.add(code)
        if _judge_candidate(strategy, "true", code, trace, feedback):
            return


    normalized = direct_law_normalization_proof(eq1_text, eq2_text)
    if normalized:
        code = make_true_code(normalized)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "direct_law_normalization", "true", code, trace, feedback
            ):
                return
    else:
        trace.append("direct_law_normalization -> no applicable normal form")


    distilled = distilled_right_projection_proof(eq1_text, eq2_text)
    if distilled:
        code = make_true_code(distilled)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "distilled_right_projection", "true", code, trace, feedback
            ):
                return
    else:
        trace.append("distilled_right_projection -> no applicable source law")

    distilled_left = distilled_left_insensitive_proof(eq1_text, eq2_text)
    if distilled_left:
        code = make_true_code(distilled_left)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "distilled_left_insensitive", "true", code, trace, feedback
            ):
                return
    else:
        trace.append("distilled_left_insensitive -> no applicable source law")

    rewrite = bounded_rewrite_proof(
        eq1_text,
        eq2_text,
    )
    if rewrite:
        code = make_true_code(rewrite)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate("bounded_rewrite", "true", code, trace, feedback):
                return
    else:
        trace.append("bounded_rewrite -> no candidate within fixed bounds")

    bidirectional = bidirectional_bounded_rewrite_proof(eq1_text, eq2_text)
    if bidirectional:
        code = make_true_code(bidirectional)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "bidirectional_rewrite", "true", code, trace, feedback
            ):
                return
    else:
        trace.append("bidirectional_rewrite -> no candidate within fixed bounds")

    n, table, complete = search_exhaustive_counterexample(
        eq1_text, eq2_text, max_n=3
    )
    if n is not None:
        code = make_false_code(n, table, eq1_text, eq2_text)
        if _judge_candidate("fin2_3_exhaustive", "false", code, trace, feedback):
            return
    else:
        trace.append(
            "fin2_3_exhaustive -> {}".format(
                "complete miss" if complete else "time limit before completion"
            )
        )

    n, table, complete = search_structured_counterexample(
        eq1_text, eq2_text
    )
    if n is not None:
        code = make_false_code(n, table, eq1_text, eq2_text)
        if _judge_candidate("fin4_7_structured", "false", code, trace, feedback):
            return
    else:
        trace.append(
            "fin4_7_structured -> {}".format(
                "complete miss" if complete else "time limit before completion"
            )
        )

    n, table, complete = search_fixed_generated_counterexample(
        eq1_text, eq2_text
    )
    if n is not None:
        code = make_false_code(n, table, eq1_text, eq2_text)
        if _judge_candidate(
            "fixed_generated_countermodels", "false", code, trace, feedback
        ):
            return
    else:
        trace.append(
            "fixed_generated_countermodels -> {}".format(
                "complete miss" if complete else "time limit before completion"
            )
        )

    n, table, complete = search_public_magma_catalog_counterexample(
        eq1_text, eq2_text
    )
    if n is not None:
        code = make_false_code(n, table, eq1_text, eq2_text)
        if _judge_candidate(
            "public_magma_catalog", "false", code, trace, feedback
        ):
            return
    else:
        trace.append(
            "public_magma_catalog -> {}".format(
                "complete miss" if complete else "time limit before completion"
            )
        )


    n, table, complete = search_large_public_counterexample(
        eq1_text, eq2_text
    )
    if n is not None:
        code = make_false_code(n, table, eq1_text, eq2_text)
        if code is not None and _judge_candidate(
            "large_public_countermodels", "false", code, trace, feedback
        ):
            return
        if code is None:
            trace.append(
                "large_public_countermodels -> structural certificate cap"
            )
    else:
        trace.append(
            "large_public_countermodels -> {}".format(
                "complete miss" if complete else "time limit before completion"
            )
        )

    n, table, complete = search_dual_number_affine_counterexample(
        eq1_text, eq2_text
    )
    if n is not None:
        code = make_false_code(n, table, eq1_text, eq2_text)
        if code is not None and _judge_candidate(
            "dual_number_affine_countermodels", "false", code, trace, feedback
        ):
            return
        if code is None:
            trace.append(
                "dual_number_affine_countermodels -> structural certificate cap"
            )
    else:
        trace.append(
            "dual_number_affine_countermodels -> {}".format(
                "complete miss" if complete else "time limit before completion"
            )
        )

    dual_reflection = dual_reflection_countermodel_code(eq1_text, eq2_text)
    if dual_reflection is not None:
        if _judge_candidate(
            "dual_reflection_countermodels",
            "false",
            dual_reflection,
            trace,
            feedback,
        ):
            return
    else:
        trace.append("dual_reflection_countermodels -> no schema witness")

    pgap_model, pgap_witness, complete = (
        search_polyhedral_guarded_action_counterexample(eq1_text, eq2_text)
    )
    if pgap_model is not None:
        code = make_polyhedral_guarded_action_false_code(
            pgap_model, pgap_witness, eq1_text, eq2_text
        )
        if code is not None and _judge_candidate(
            "polyhedral_guarded_action_countermodels",
            "false",
            code,
            trace,
            feedback,
        ):
            return
        if code is None:
            trace.append(
                "polyhedral_guarded_action_countermodels -> certificate cap"
            )
    else:
        trace.append(
            "polyhedral_guarded_action_countermodels -> {}".format(
                "complete miss" if complete else "time limit before completion"
            )
        )

    goal_paramodulation = goal_directed_paramodulation_proof(
        eq1_text, eq2_text
    )
    if goal_paramodulation:
        code = make_true_code(goal_paramodulation)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "goal_directed_paramodulation",
                "true",
                code,
                trace,
                feedback,
            ):
                return
    else:
        trace.append(
            "goal_directed_paramodulation -> no candidate within fixed bounds"
        )

    symbolic = symbolic_narrowing_proof(eq1_text, eq2_text)
    if symbolic:
        code = make_true_code(symbolic)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "symbolic_narrowing", "true", code, trace, feedback
            ):
                return
    else:
        trace.append("symbolic_narrowing -> no candidate within fixed bounds")

    beam = goal_guided_symbolic_beam_proof(eq1_text, eq2_text)
    if beam:
        code = make_true_code(beam)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "goal_guided_symbolic_beam", "true", code, trace, feedback
            ):
                return
    else:
        trace.append(
            "goal_guided_symbolic_beam -> no candidate within fixed bounds"
        )

    late_goal_paramodulation = late_goal_directed_paramodulation_proof(
        eq1_text, eq2_text
    )
    if late_goal_paramodulation:
        code = make_true_code(late_goal_paramodulation)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "late_goal_directed_paramodulation",
                "true",
                code,
                trace,
                feedback,
            ):
                return
    else:
        trace.append(
            "late_goal_directed_paramodulation -> no candidate within fixed bounds"
        )

    deep_goal_paramodulation = deep_goal_directed_paramodulation_proof(
        eq1_text, eq2_text
    )
    if deep_goal_paramodulation:
        code = make_true_code(deep_goal_paramodulation)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "deep_goal_directed_paramodulation",
                "true",
                code,
                trace,
                feedback,
            ):
                return
    else:
        trace.append(
            "deep_goal_directed_paramodulation -> no candidate within fixed bounds"
        )
    product_collapse = product_collapse_bridge_proof(eq1_text, eq2_text)
    if product_collapse:
        code = make_true_code(product_collapse)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "product_collapse_bridge",
                "true",
                code,
                trace,
                feedback,
            ):
                return
    else:
        trace.append(
            "product_collapse_bridge -> no candidate within structural gate"
        )

    extended_goal_paramodulation = extended_goal_directed_paramodulation_proof(
        eq1_text, eq2_text
    )
    if extended_goal_paramodulation:
        code = make_true_code(extended_goal_paramodulation)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "extended_goal_directed_paramodulation",
                "true",
                code,
                trace,
                feedback,
            ):
                return
    else:
        trace.append(
            "extended_goal_directed_paramodulation -> no candidate within fixed bounds"
        )

    if _hypothesis_has_variable_side(eq1_text):
        trace.append(
            "deep_goal_guided_symbolic_beam -> skipped variable-side hypothesis"
        )
    else:
        deep_beam = deep_goal_guided_symbolic_beam_proof(eq1_text, eq2_text)
        if deep_beam:
            code = make_true_code(deep_beam)
            if code not in tried_code:
                tried_code.add(code)
                if _judge_candidate(
                    "deep_goal_guided_symbolic_beam",
                    "true",
                    code,
                    trace,
                    feedback,
                ):
                    return
        else:
            trace.append(
                "deep_goal_guided_symbolic_beam -> no candidate within fixed bounds"
            )

    # This broad singleton search is deliberately last among deterministic
    # proof lanes.  It remains a sound fallback, but visible hard3 profiling
    # found zero first hits across 156 calls while later goal-directed lanes
    # solved 152 of those cases.  Delaying it preserves coverage and avoids
    # spending most of the proof-search budget before the high-yield methods.
    derived_singleton = derived_singleton_paramodulation_proof(
        eq1_text, eq2_text
    )
    if derived_singleton:
        code = make_true_code(derived_singleton)
        if code not in tried_code:
            tried_code.add(code)
            if _judge_candidate(
                "derived_singleton_paramodulation",
                "true",
                code,
                trace,
                feedback,
            ):
                return
    else:
        trace.append(
            "derived_singleton_paramodulation -> no candidate within fixed bounds"
        )

    # No direct model/API request occurs here.  This final stage asks only the
    # organizer's protocol proxy, which may return an immediate local error
    # when no configured/free route is available.
    _llm_fallback(problem, eq1_text, eq2_text, trace, feedback)

import hashlib
from collections import Counter
from contextlib import contextmanager
from dataclasses import dataclass, field
import signal
import threading
import time
from typing import Any, Callable, Iterable, Iterator, Sequence

_ORIGINAL_LLM_FALLBACK = _llm_fallback

MAX_DEPTH = 18

MAX_RULES = 2_048

MAX_CANDIDATES = 8_192

MAX_QUEUE = 131_072

MAX_TERM_SIZE = 45

MAX_DEMODULATION_REWRITES_PER_SIDE = 8

MAX_LEAN_CODE_BYTES = 100_000

def _operation_count(term) -> int:
    if term[0] == VAR:
        return 0
    return 1 + _operation_count(term[1]) + _operation_count(term[2])


def structural_trigger(eq1_text: str, eq2_text: str) -> bool:
    """Apply only the exact preregistered, equation-structure-only gate."""
    hypothesis = parse_equation(eq1_text)
    goal = parse_equation(eq2_text)
    bare_sides = sum(term[0] == VAR for term in hypothesis[:2])
    nonvariable = [term for term in hypothesis[:2] if term[0] != VAR]
    return bool(
        bare_sides == 1
        and len(nonvariable) == 1
        and _operation_count(nonvariable[0]) == 4
        and 2 <= len(hypothesis[2]) <= 3
        and _operation_count(goal[0]) + _operation_count(goal[1]) <= 4
        and len(goal[2]) <= 4
    )


def deep_right_branch_demodulation_trigger(eq1_text: str, eq2_text: str) -> bool:
    """Select the narrow five-operation family where demodulation is cheap."""
    hypothesis = parse_equation(eq1_text)
    goal = parse_equation(eq2_text)
    hypothesis_terms = [term for term in hypothesis[:2] if term[0] != VAR]
    goal_terms = [term for term in goal[:2] if term[0] != VAR]
    if (
        sum(term[0] == VAR for term in hypothesis[:2]) != 1
        or len(hypothesis_terms) != 1
        or sum(term[0] == VAR for term in goal[:2]) != 1
        or len(goal_terms) != 1
    ):
        return False
    hypothesis_term = hypothesis_terms[0]
    goal_term = goal_terms[0]
    return bool(
        _operation_count(hypothesis_term) == 5
        and len(hypothesis[2]) == 3
        and _term_depth(hypothesis_term) == 6
        and hypothesis_term[1][0] == VAR
        and hypothesis_term[2][0] == OP
        and _operation_count(goal_term) == 5
        and len(goal[2]) == 3
        and _term_depth(goal_term) <= 4
    )


_SINGLETON_FORCING_SOURCE_TEXT = "x = (y * z) * ((x * (x * y)) * z)"

_SINGLETON_FORCING_SOURCE = canonical_equation(
    _SINGLETON_FORCING_SOURCE_TEXT
)

SINGLETON_FORCING_COLLAPSE_PROOF = decompress(b85decode(
    "c-pO4L2}zL47}$RIEt4HNlCHY8D*xYzC+HWaSw4ij;e`Y&?oeNeMv=%lt==kNT-*`mMJW-02WYwoQKOB^l-d8_2V;~I8-BtQNSqS3w&eKpGw{N`{(y`m+9+tL(U(}b>xiM6AU{2YzN2d9l-NP|1>~#y8cvmwP|+$etms4cp`x}eGmp`zK+u1xWEfC30zfENRz!hTl%hc?|!)S=Xa={-p((Vua_67zW+MI0No?p;@-eu_C&frYQC7qhqQbwWGw7+=4WBeiVA)4YCX<KGF*G3AfL<NAm)_{lsG>uhn9r6ZfH!8hgu(4NkDkqXTftH6VWM1%!UBcaOm3>8v_Q+BaOS&Ax)j4Gl(218>(%>KAq~(6zXOXVfu72cXXnYWhI!da^ks?vI;^-mz8AYMQZq-J20fT4XQ7&<7L|Z(9!wDT&e7hVGrEUa>$E0tlDj18&T6nbp;2r%6$9;8SjSnn81AjDhNF4X^!YfM0lt;%|4$ato@vj9d|SplQpG`oLeN&CrB&_Wr*mvz+@f}nW^}@6`jzR@_~ZHrqcPf4ez<y^3YYsQra;cr|x9}?qJ~-Ah9{z9WYl}V#CXuQw5_+54pr@;}0gw5XzbnPoGWcYbPOzk$4n8G?z+{SB+ed>a7wpOQDE?i7fr`N=>I#5E5IrP0Sr{Q*->{L_JMGjUxRhqGw(NW~Zz-`#Nut=l;SfgGHXl_Gtr`yDR4_HSw#lu@<Akmsr6YQAau%X&j-_W=#~^OEWJhn_OfanI!6}kunyPtJfU~K*XX*(rPJgm?BOl(%Mq#3LM4On*VUvN1Ir%(%jLi(vWkMw(`HTx>e048-$QP91aD{;ELE_=F`0znIOgk6P@&4`5Bfjm4AOq?l>n0Na9T;K2j8kk@4Kt-s@J<e2|(Q7oLmWx<LA2)69!ntkPsq_%gY%kQ%0(MzUq(RN(2l<Dr&LUr5ulWz4Yh(x%q_7f4y{;mH00!+E%-"
)).decode("utf-8")


def singleton_forcing_source_trigger(eq1_text: str, eq2_text: str) -> bool:
    """Recognize a source law that forces every two carrier elements equal."""
    del eq2_text
    return canonical_equation(eq1_text) == _SINGLETON_FORCING_SOURCE


def expanded_cap_proof(eq1_text: str, eq2_text: str):
    """Run Stage A with the exact preregistered doubled work caps."""
    return extended_goal_directed_paramodulation_proof(
        eq1_text,
        eq2_text,
        max_depth=MAX_DEPTH,
        max_rules=MAX_RULES,
        max_candidates=MAX_CANDIDATES,
        max_queue=MAX_QUEUE,
        max_term_size=MAX_TERM_SIZE,
    )


def _term_depth(term) -> int:
    if term[0] == VAR:
        return 1
    return 1 + max(_term_depth(term[1]), _term_depth(term[2]))


def _reduction_key(term):
    return (term_size(term), _term_depth(term), repr(term))


def _innermost_leftmost_paths(term, path=()):
    if term[0] == OP:
        yield from _innermost_leftmost_paths(term[1], path + (0,))
        yield from _innermost_leftmost_paths(term[2], path + (1,))
    yield path, term


def _proof_application(index: int, arguments, symmetric: bool = False) -> str:
    return _paramod_application(index, arguments, symmetric)


def _demodulations(
    outer_index: int,
    rule_index: int,
    outer,
    rule,
) -> Iterator[tuple[tuple, str, int]]:
    """Yield replayable, strictly decreasing one-step unit demodulations.

    Matching is one-way: selected-rule variables are instantiated by a
    concrete subterm of the outer equation.  The emitted equality proof is
    reconstructed from the two parent theorems plus congruence and
    transitivity.  Canonicalization is performed only after the concrete
    reduction-order check.
    """
    outer_variables = variables_in_order(*outer)
    rule_variables = variables_in_order(*rule)
    seen = set()
    for outer_side in (0, 1):
        outer_source = outer[outer_side]
        outer_other = outer[1 - outer_side]
        for path, subtree in _innermost_leftmost_paths(outer_source):
            for rule_symmetric, pattern, replacement_pattern in (
                (False, rule[0], rule[1]),
                (True, rule[1], rule[0]),
            ):
                substitution = {}
                if not _match_pattern(pattern, subtree, substitution):
                    continue
                if any(variable not in substitution for variable in rule_variables):
                    continue
                replacement = _instantiate(
                    replacement_pattern, substitution
                )
                if not _reduction_key(replacement) < _reduction_key(subtree):
                    continue
                replaced = _replace_at_path(
                    outer_source, path, replacement
                )
                if replaced == outer_source:
                    continue
                if max(term_size(replaced), term_size(outer_other)) > (
                    MAX_TERM_SIZE
                ):
                    continue
                raw_left, raw_right = (
                    (replaced, outer_other)
                    if outer_side == 0
                    else (outer_other, replaced)
                )
                equation, names, swapped = _paramod_canonicalize(
                    raw_left, raw_right
                )
                equation_variables = variables_in_order(*equation)
                if not equation_variables:
                    continue
                filler = (VAR, equation_variables[0])
                mapped_source = _paramod_map_variables(
                    outer_source, names, filler
                )
                outer_arguments = [
                    _paramod_map_variables(
                        (VAR, variable), names, filler
                    )
                    for variable in outer_variables
                ]
                rule_arguments = [
                    _paramod_map_variables(
                        substitution[variable], names, filler
                    )
                    for variable in rule_variables
                ]
                outer_proof = _proof_application(
                    outer_index, outer_arguments
                )
                rule_proof = _proof_application(
                    rule_index, rule_arguments, rule_symmetric
                )
                rewrite_proof = _wrap_congruence(
                    mapped_source, path, rule_proof
                )
                if outer_side == 0:
                    proof = "({}).symm.trans ({})".format(
                        rewrite_proof, outer_proof
                    )
                else:
                    proof = "({}).trans ({})".format(
                        outer_proof, rewrite_proof
                    )
                if swapped:
                    proof = "({}).symm".format(proof)
                key = (equation, proof, outer_side)
                if key in seen:
                    continue
                seen.add(key)
                yield equation, proof, outer_side


@dataclass(frozen=True)
class _Node:
    equation: tuple
    proof: str
    kind: str
    parents: tuple[int, ...]
    serial: int
    depth: int


@dataclass(frozen=True)
class _Queued:
    equation: tuple
    proof: str
    kind: str
    parents: tuple[int, ...]
    serial: int
    depth: int


def _node_replays(index: int, nodes: list[_Node], parsed_hypothesis) -> bool:
    if not 0 <= index < len(nodes):
        return False
    node = nodes[index]
    if node.kind == "initial":
        return bool(
            index == 0
            and not node.parents
            and node.proof
            == _paramod_initial_proof(parsed_hypothesis, node.equation)
        )
    if not node.parents or any(
        not isinstance(value, int) or not 0 <= value < index
        for value in node.parents
    ):
        return False
    if node.kind == "paramod" and len(node.parents) == 2:
        outer_index, inner_index = node.parents
        for equation, proof, _source in _paramodulations(
            outer_index,
            inner_index,
            nodes[outer_index].equation,
            nodes[inner_index].equation,
            node.serial,
            MAX_TERM_SIZE,
        ):
            if equation == node.equation and proof == node.proof:
                return True
        return False
    if node.kind == "demod" and len(node.parents) == 2:
        outer_index, rule_index = node.parents
        return any(
            equation == node.equation and proof == node.proof
            for equation, proof, _side in _demodulations(
                outer_index,
                rule_index,
                nodes[outer_index].equation,
                nodes[rule_index].equation,
            )
        )
    return False


def _equation_subsumed(equation, selected: list[int], nodes: list[_Node]) -> bool:
    target = (equation[0], equation[1], variables_in_order(*equation))
    for index in selected:
        pattern_equation = nodes[index].equation
        pattern = (
            pattern_equation[0],
            pattern_equation[1],
            variables_in_order(*pattern_equation),
        )
        if _direct_instance(pattern, target) is not None:
            return True
    return False


def _render_goal_proof(
    eq2_text: str,
    parsed_hypothesis,
    nodes: list[_Node],
    goal_index: int,
):
    parsed_goal = parse_equation(eq2_text)
    match = _paramod_goal_match(nodes[goal_index].equation, parsed_goal)
    if match is None:
        return None
    substitution, symmetric = match
    needed = set()
    visiting = set()

    def include(index: int) -> bool:
        if index in needed:
            return True
        if not 0 <= index < len(nodes) or index in visiting:
            return False
        visiting.add(index)
        needed.add(index)
        for dependency in nodes[index].parents:
            if not include(dependency):
                return False
        visiting.remove(index)
        return True

    if not include(goal_index):
        return None
    if any(
        not _node_replays(index, nodes, parsed_hypothesis)
        for index in sorted(needed)
    ):
        return None
    lines = [_intro_line(parsed_goal[2])]
    for index in sorted(needed):
        equation = nodes[index].equation
        variables = variables_in_order(*equation)
        if not variables:
            return None
        lines.append(
            "have h{} ({} : G) : {} = {} := by".format(
                index,
                " ".join(variables),
                render_term(equation[0]),
                render_term(equation[1]),
            )
        )
        lines.append("  exact {}".format(nodes[index].proof))
    goal_variables = variables_in_order(*nodes[goal_index].equation)
    if any(variable not in substitution for variable in goal_variables):
        return None
    arguments = [substitution[variable] for variable in goal_variables]
    exact = _proof_application(goal_index, arguments, symmetric)
    lines.append("exact {}".format(exact))
    return "\n".join(line for line in lines if line)


def demodulating_goal_paramodulation_proof(eq1_text: str, eq2_text: str):
    """Run Stage B with replayed paramodulation and ordered demodulation."""
    parsed_hypothesis = parse_equation(eq1_text)
    parsed_goal = parse_equation(eq2_text)
    if max(
        term_size(parsed_hypothesis[0]),
        term_size(parsed_hypothesis[1]),
    ) > MAX_TERM_SIZE:
        return None
    initial, _, _ = _paramod_canonicalize(
        parsed_hypothesis[0], parsed_hypothesis[1]
    )
    initial_proof = _paramod_initial_proof(parsed_hypothesis, initial)
    if initial_proof is None:
        return None
    nodes = [
        _Node(initial, initial_proof, "initial", (), 0, 0)
    ]
    selected = [0]
    selected_keys = {initial}
    queued_keys = set()
    candidates = []
    ordinal = 0
    serial = 0
    generated_candidates = 0
    work_cap_hit = False

    def push(candidate: _Queued) -> None:
        nonlocal generated_candidates, ordinal, work_cap_hit
        if generated_candidates >= MAX_CANDIDATES:
            work_cap_hit = True
            return
        if (
            candidate.depth > MAX_DEPTH
            or candidate.equation in selected_keys
            or candidate.equation in queued_keys
            or candidate.equation[0] == candidate.equation[1]
        ):
            return
        if len(queued_keys) >= MAX_QUEUE:
            work_cap_hit = True
            return
        queued_keys.add(candidate.equation)
        generated_candidates += 1
        ordinal += 1
        heapq.heappush(
            candidates,
            (
                _paramod_score(
                    candidate.equation, candidate.depth, parsed_goal
                ),
                ordinal,
                candidate,
            ),
        )

    def enqueue_paramod(outer_index: int, inner_index: int) -> None:
        nonlocal serial
        if work_cap_hit:
            return
        depth = max(
            nodes[outer_index].depth, nodes[inner_index].depth
        ) + 1
        if depth > MAX_DEPTH:
            return
        serial += 1
        for equation, proof, _source in _paramodulations(
            outer_index,
            inner_index,
            nodes[outer_index].equation,
            nodes[inner_index].equation,
            serial,
            MAX_TERM_SIZE,
        ):
            push(
                _Queued(
                    equation,
                    proof,
                    "paramod",
                    (outer_index, inner_index),
                    serial,
                    depth,
                )
            )
            if work_cap_hit:
                break

    def enqueue_backward_demod(outer_index: int, rule_index: int) -> None:
        if work_cap_hit:
            return
        depth = max(nodes[outer_index].depth, nodes[rule_index].depth) + 1
        if depth > MAX_DEPTH:
            return
        for equation, proof, _side in _demodulations(
            outer_index,
            rule_index,
            nodes[outer_index].equation,
            nodes[rule_index].equation,
        ):
            push(
                _Queued(
                    equation,
                    proof,
                    "demod",
                    (outer_index, rule_index),
                    0,
                    depth,
                )
            )
            if work_cap_hit:
                break

    def append_node(candidate: _Queued):
        node = _Node(
            candidate.equation,
            candidate.proof,
            candidate.kind,
            candidate.parents,
            candidate.serial,
            candidate.depth,
        )
        nodes.append(node)
        index = len(nodes) - 1
        if not _node_replays(index, nodes, parsed_hypothesis):
            nodes.pop()
            return None
        return index

    def normalize_on_pop(index: int):
        seen = {nodes[index].equation}
        current = index
        for side in (0, 1):
            rewrites = 0
            while rewrites < MAX_DEMODULATION_REWRITES_PER_SIDE:
                chosen = None
                for rule_index in selected:
                    for equation, proof, rewritten_side in _demodulations(
                        current,
                        rule_index,
                        nodes[current].equation,
                        nodes[rule_index].equation,
                    ):
                        if rewritten_side != side or equation in seen:
                            continue
                        depth = max(
                            nodes[current].depth, nodes[rule_index].depth
                        ) + 1
                        if depth > MAX_DEPTH:
                            continue
                        chosen = _Queued(
                            equation,
                            proof,
                            "demod",
                            (current, rule_index),
                            0,
                            depth,
                        )
                        break
                    if chosen is not None:
                        break
                if chosen is None:
                    break
                next_index = append_node(chosen)
                if next_index is None:
                    return None
                current = next_index
                seen.add(nodes[current].equation)
                rewrites += 1
                if nodes[current].equation[0] == nodes[current].equation[1]:
                    return current
        return current

    initial_match = _paramod_goal_match(initial, parsed_goal)
    if initial_match is not None:
        return _render_goal_proof(
            eq2_text, parsed_hypothesis, nodes, 0
        )
    enqueue_paramod(0, 0)
    processed = 0
    while (
        candidates
        and len(selected) < MAX_RULES
        and processed < MAX_CANDIDATES
        and not work_cap_hit
    ):
        _score, _ordinal, candidate = heapq.heappop(candidates)
        queued_keys.discard(candidate.equation)
        processed += 1
        if candidate.equation in selected_keys:
            continue
        raw_index = append_node(candidate)
        if raw_index is None:
            continue
        normalized_index = normalize_on_pop(raw_index)
        if normalized_index is None:
            continue
        equation = nodes[normalized_index].equation
        if equation[0] == equation[1] or equation in selected_keys:
            continue
        if _equation_subsumed(equation, selected, nodes):
            continue
        selected.append(normalized_index)
        selected_keys.add(equation)
        if _paramod_goal_match(equation, parsed_goal) is not None:
            return _render_goal_proof(
                eq2_text, parsed_hypothesis, nodes, normalized_index
            )
        previous = selected[:-1]
        for old_index in previous + [normalized_index]:
            enqueue_paramod(normalized_index, old_index)
            if work_cap_hit:
                break
            if old_index != normalized_index:
                enqueue_paramod(old_index, normalized_index)
            if work_cap_hit:
                break
        if work_cap_hit:
            break
        for old_index in previous:
            if old_index != 0:
                enqueue_backward_demod(old_index, normalized_index)
            if work_cap_hit:
                break
    return None


def singleton_forcing_source_proof(eq1_text: str, eq2_text: str):
    """Replay the distilled collapse lemma, then instantiate the goal."""
    if not singleton_forcing_source_trigger(eq1_text, eq2_text):
        return None
    source_proof = _source_law_instance_proof(
        eq1_text, _SINGLETON_FORCING_SOURCE_TEXT
    )
    if not source_proof:
        return None
    goal_left, goal_right, goal_variables = parse_equation(eq2_text)
    lines = _distilled_source_lines(
        "singleton_source",
        _SINGLETON_FORCING_SOURCE_TEXT,
        source_proof,
    )
    lines.append(_intro_line(goal_variables))
    lines.append("have collapse : ∀ a b : G, a = b := by")
    collapse_body = re.sub(
        r"\bhyp\b",
        "singleton_source",
        SINGLETON_FORCING_COLLAPSE_PROOF,
    )
    lines.extend("  " + line for line in collapse_body.splitlines())
    lines.append(
        "exact collapse {} {}".format(
            render_term(goal_left), render_term(goal_right)
        )
    )
    return "\n".join(line for line in lines if line)


def _try_true_candidate(strategy: str, proof, trace, feedback) -> bool:
    if not proof:
        trace.append("{} -> no candidate within fixed bounds".format(strategy))
        return False
    code = make_true_code(proof)
    if len(code.encode("utf-8")) > MAX_LEAN_CODE_BYTES:
        trace.append("{} -> certificate exceeds fixed byte cap".format(strategy))
        return False
    return _judge_candidate(
        strategy, "true", code, trace, feedback
    )


def _h19_fallback(problem, eq1_text, eq2_text, trace, feedback):
    if structural_trigger(eq1_text, eq2_text):
        if _try_true_candidate(
            "h19_expanded_goal_paramodulation",
            expanded_cap_proof(eq1_text, eq2_text),
            trace,
            feedback,
        ):
            return True
        if _try_true_candidate(
            "h19_demodulating_goal_paramodulation",
            demodulating_goal_paramodulation_proof(eq1_text, eq2_text),
            trace,
            feedback,
        ):
            return True
    elif deep_right_branch_demodulation_trigger(eq1_text, eq2_text):
        if _try_true_candidate(
            "deep_right_branch_demodulating_goal_paramodulation",
            demodulating_goal_paramodulation_proof(eq1_text, eq2_text),
            trace,
            feedback,
        ):
            return True
    else:
        trace.append("h19_demodulating_goal_paramodulation -> structural gate miss")
    return _ORIGINAL_LLM_FALLBACK(
        problem, eq1_text, eq2_text, trace, feedback
    )

_llm_fallback = _h19_fallback

MAX_RESPONSE_CHARACTERS = 131_072

MAX_CANDIDATE_OBJECTS = 16

MAX_CHAINS_PER_RESPONSE = 4

MAX_WAYPOINTS_PER_CHAIN = 2

MAX_UNIQUE_WAYPOINTS_PER_RESPONSE = 8

MAX_WAYPOINT_TEXT_CHARACTERS = 512

MAX_VARIABLES_PER_WAYPOINT = 5

MAX_OPERATIONS_PER_WAYPOINT_SIDE = 8

MAX_LEAN_CODE_BYTES = 100_000

FAILURE_CATEGORIES = (
    "transport_error",
    "empty_response",
    "truncated_response",
    "no_json_object",
    "schema_error",
    "term_parse_error",
    "term_cap_error",
    "duplicate_waypoint",
    "degenerate_waypoint",
    "forward_link_unproved",
    "middle_link_unproved",
    "goal_link_unproved",
    "composition_replay_error",
    "certificate_byte_cap",
    "lean_judge_rejection",
    "accepted",
)

def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()

class WaypointProtocolError(ValueError):
    def __init__(self, category: str, detail: str):
        if category not in FAILURE_CATEGORIES:
            raise ValueError(f"unknown H21 failure category: {category}")
        self.category = category
        self.detail = re.sub(r"\s+", " ", str(detail)).strip()[:500]
        super().__init__(f"{category}: {self.detail}")


class DuplicateJsonKeyError(ValueError):
    pass


@dataclass(frozen=True)
class ExtractionResult:
    objects: tuple[dict[str, Any], ...]
    scanned_characters: int
    response_truncated: bool
    object_limit_reached: bool
    error_category: str | None


@dataclass(frozen=True)
class Waypoint:
    normalized_text: str
    canonical_key: tuple[Any, Any]


@dataclass(frozen=True)
class BridgeChain:
    waypoints: tuple[Waypoint, ...]


@dataclass(frozen=True)
class BridgePlan:
    chains: tuple[BridgeChain, ...]
    digest: str


@dataclass(frozen=True)
class LinkProof:
    engine: str
    proof_body: str


@dataclass(frozen=True)
class VerifiedCandidate:
    verdict: str
    code: str
    digest: str
    link_count: int
    engine_counts: dict[str, int]


@dataclass(frozen=True)
class CandidateAttempt:
    object_index: int
    chain_index: int | None
    category: str
    proved_links: int


@dataclass(frozen=True)
class ResponseVerification:
    extraction: ExtractionResult
    attempts: tuple[CandidateAttempt, ...]
    candidate: VerifiedCandidate | None
    plan_digest: str | None


LinkEngine = tuple[str, Callable[[str, str], Any]]


def _strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateJsonKeyError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def extract_json_objects(
    text: Any,
    *,
    provider_truncated: bool = False,
    maximum_characters: int = MAX_RESPONSE_CHARACTERS,
    maximum_objects: int = MAX_CANDIDATE_OBJECTS,
) -> ExtractionResult:
    if not isinstance(text, str) or not text.strip():
        return ExtractionResult(
            objects=(),
            scanned_characters=0 if not isinstance(text, str) else len(text),
            response_truncated=bool(provider_truncated),
            object_limit_reached=False,
            error_category="empty_response",
        )
    if maximum_characters < 1 or maximum_objects < 1:
        raise ValueError("H21 extraction limits must be positive")
    clipped = text[:maximum_characters]
    response_truncated = bool(provider_truncated or len(text) > len(clipped))
    if response_truncated:
        return ExtractionResult(
            objects=(),
            scanned_characters=len(clipped),
            response_truncated=True,
            object_limit_reached=False,
            error_category="truncated_response",
        )
    decoder = json.JSONDecoder(object_pairs_hook=_strict_pairs)
    objects: list[dict[str, Any]] = []
    cursor = 0
    object_limit_reached = False
    while cursor < len(clipped):
        if len(objects) >= maximum_objects:
            object_limit_reached = True
            break
        brace = clipped.find("{", cursor)
        quote = clipped.find('"', cursor)
        positions = [position for position in (brace, quote) if position >= 0]
        if not positions:
            break
        position = min(positions)
        if position == quote and (brace < 0 or quote < brace):
            try:
                quoted, end = decoder.raw_decode(clipped, quote)
            except (DuplicateJsonKeyError, TypeError, ValueError):
                cursor = quote + 1
                continue
            cursor = max(end, quote + 1) if isinstance(quoted, str) else quote + 1
            continue
        try:
            candidate, end = decoder.raw_decode(clipped, brace)
        except (DuplicateJsonKeyError, TypeError, ValueError):
            cursor = brace + 1
            continue
        cursor = max(end, brace + 1)
        if isinstance(candidate, dict):
            objects.append(candidate)
    return ExtractionResult(
        objects=tuple(objects),
        scanned_characters=len(clipped),
        response_truncated=False,
        object_limit_reached=object_limit_reached,
        error_category=None if objects else "no_json_object",
    )


def _require_exact_keys(value: dict[str, Any], required: Iterable[str]) -> None:
    expected = set(required)
    actual = set(value)
    if actual != expected:
        raise WaypointProtocolError(
            "schema_error",
            "exact keys required; missing={}; extra={}".format(
                sorted(expected - actual), sorted(actual - expected)
            ),
        )


def _operation_count(term: Any) -> int:
    if term[0] == VAR:
        return 0
    return 1 + _operation_count(term[1]) + _operation_count(term[2])


def _rename_term(term: Any, names: dict[str, str]) -> Any:
    if term[0] == VAR:
        return (VAR, names[term[1]])
    return (
        OP,
        _rename_term(term[1], names),
        _rename_term(term[2], names),
    )


def _normalize_equation(parsed: tuple[Any, Any, Sequence[str]]) -> str:
    variables = list(parsed[2])
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if len(variables) > len(alphabet):
        raise WaypointProtocolError(
            "term_cap_error", "equation has too many variables to normalize"
        )
    names = {name: alphabet[index] for index, name in enumerate(variables)}
    left = _rename_term(parsed[0], names)
    right = _rename_term(parsed[1], names)
    return f"{render_term(left)} = {render_term(right)}"


def _parse_waypoint(
    value: dict[str, Any],
    *,
    source_key: tuple[Any, Any],
    target_key: tuple[Any, Any],
) -> Waypoint:
    _require_exact_keys(value, ("left", "right"))
    left = value.get("left")
    right = value.get("right")
    if not isinstance(left, str) or not isinstance(right, str):
        raise WaypointProtocolError(
            "schema_error", "waypoint left and right must be strings"
        )
    if not left.strip() or not right.strip():
        raise WaypointProtocolError(
            "term_parse_error", "waypoint sides must be nonempty"
        )
    if max(len(left), len(right)) > MAX_WAYPOINT_TEXT_CHARACTERS:
        raise WaypointProtocolError(
            "term_cap_error",
            f"waypoint side exceeds {MAX_WAYPOINT_TEXT_CHARACTERS} characters",
        )
    text = f"{left} = {right}"
    try:
        parsed = parse_equation(text)
    except (TypeError, ValueError) as exc:
        raise WaypointProtocolError("term_parse_error", str(exc)) from exc
    left_operations = _operation_count(parsed[0])
    right_operations = _operation_count(parsed[1])
    if max(left_operations, right_operations) > MAX_OPERATIONS_PER_WAYPOINT_SIDE:
        raise WaypointProtocolError(
            "term_cap_error",
            "waypoint side operation count exceeds {}".format(
                MAX_OPERATIONS_PER_WAYPOINT_SIDE
            ),
        )
    if len(parsed[2]) > MAX_VARIABLES_PER_WAYPOINT:
        raise WaypointProtocolError(
            "term_cap_error",
            f"waypoint uses more than {MAX_VARIABLES_PER_WAYPOINT} variables",
        )
    if parsed[0] == parsed[1]:
        raise WaypointProtocolError(
            "degenerate_waypoint", "waypoint has syntactically equal sides"
        )
    canonical_key = canonical_equation(text)
    if canonical_key == source_key:
        raise WaypointProtocolError(
            "degenerate_waypoint", "waypoint is alpha-equivalent to the source"
        )
    if canonical_key == target_key:
        raise WaypointProtocolError(
            "degenerate_waypoint", "waypoint is alpha-equivalent to the target"
        )
    return Waypoint(
        normalized_text=_normalize_equation(parsed),
        canonical_key=canonical_key,
    )


def parse_bridge_plan(
    eq1_text: str,
    eq2_text: str,
    value: dict[str, Any],
) -> BridgePlan:
    _require_exact_keys(value, ("chains",))
    chains_value = value.get("chains")
    if not isinstance(chains_value, list) or not (
        1 <= len(chains_value) <= MAX_CHAINS_PER_RESPONSE
    ):
        raise WaypointProtocolError(
            "schema_error",
            f"chains must contain 1..{MAX_CHAINS_PER_RESPONSE} objects",
        )
    try:
        source_key = canonical_equation(eq1_text)
        target_key = canonical_equation(eq2_text)
    except (TypeError, ValueError) as exc:
        raise WaypointProtocolError("term_parse_error", str(exc)) from exc
    seen: set[tuple[Any, Any]] = set()
    chains: list[BridgeChain] = []
    digest_shape: list[dict[str, Any]] = []
    for chain_index, chain_value in enumerate(chains_value):
        if not isinstance(chain_value, dict):
            raise WaypointProtocolError(
                "schema_error", f"chain {chain_index} must be an object"
            )
        _require_exact_keys(chain_value, ("waypoints",))
        waypoints_value = chain_value.get("waypoints")
        if not isinstance(waypoints_value, list) or not (
            1 <= len(waypoints_value) <= MAX_WAYPOINTS_PER_CHAIN
        ):
            raise WaypointProtocolError(
                "schema_error",
                "chain {} waypoints must contain 1..{} objects".format(
                    chain_index, MAX_WAYPOINTS_PER_CHAIN
                ),
            )
        waypoints: list[Waypoint] = []
        for waypoint_index, waypoint_value in enumerate(waypoints_value):
            if not isinstance(waypoint_value, dict):
                raise WaypointProtocolError(
                    "schema_error",
                    f"chain {chain_index} waypoint {waypoint_index} must be an object",
                )
            waypoint = _parse_waypoint(
                waypoint_value,
                source_key=source_key,
                target_key=target_key,
            )
            if waypoint.canonical_key in seen:
                raise WaypointProtocolError(
                    "duplicate_waypoint",
                    "duplicate or alpha/reversal-equivalent waypoint",
                )
            seen.add(waypoint.canonical_key)
            waypoints.append(waypoint)
        chains.append(BridgeChain(tuple(waypoints)))
        digest_shape.append(
            {"waypoints": [item.canonical_key for item in waypoints]}
        )
    if len(seen) > MAX_UNIQUE_WAYPOINTS_PER_RESPONSE:
        raise WaypointProtocolError(
            "term_cap_error",
            "response exceeds {} unique waypoints".format(
                MAX_UNIQUE_WAYPOINTS_PER_RESPONSE
            ),
        )
    digest_payload = json.dumps(
        {"chains": digest_shape},
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return BridgePlan(tuple(chains), sha256_bytes(digest_payload))


DEFAULT_LINK_ENGINES: tuple[LinkEngine, ...] = (
    ("expanded_goal_paramodulation", expanded_cap_proof),
    ("demodulating_goal_paramodulation", demodulating_goal_paramodulation_proof),
)


def prove_link(
    source_text: str,
    target_text: str,
    *,
    engines: Sequence[LinkEngine] = DEFAULT_LINK_ENGINES,
) -> LinkProof | None:
    for name, engine in engines:
        try:
            proof = engine(source_text, target_text)
        except Exception as exc:
            raise WaypointProtocolError(
                "composition_replay_error",
                f"frozen link engine {name} raised {type(exc).__name__}",
            ) from exc
        if proof is None:
            continue
        if not isinstance(proof, str) or not proof.strip():
            raise WaypointProtocolError(
                "composition_replay_error",
                f"frozen link engine {name} returned an invalid proof body",
            )
        return LinkProof(name, proof)
    return None


def _identifier_character(char: str) -> bool:
    return char == "_" or char == "'" or char.isalnum()


def rename_lean_identifier(text: str, source: str, replacement: str) -> str:
    """Rename an exact Lean identifier outside comments and string literals."""
    if not source or not replacement:
        raise ValueError("Lean identifier names must be nonempty")
    output: list[str] = []
    index = 0
    block_depth = 0
    in_string = False
    escaped = False
    while index < len(text):
        if block_depth:
            if text.startswith("/-", index):
                block_depth += 1
                output.append("/-")
                index += 2
                continue
            if text.startswith("-/", index):
                block_depth -= 1
                output.append("-/")
                index += 2
                continue
            output.append(text[index])
            index += 1
            continue
        if in_string:
            char = text[index]
            output.append(char)
            index += 1
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if text.startswith("--", index):
            end = text.find("\n", index)
            if end < 0:
                output.append(text[index:])
                break
            output.append(text[index:end])
            index = end
            continue
        if text.startswith("/-", index):
            block_depth = 1
            output.append("/-")
            index += 2
            continue
        if text[index] == '"':
            in_string = True
            output.append('"')
            index += 1
            continue
        char = text[index]
        if char.isalpha() or char == "_":
            end = index + 1
            while end < len(text) and _identifier_character(text[end]):
                end += 1
            token = text[index:end]
            output.append(replacement if token == source else token)
            index = end
            continue
        output.append(char)
        index += 1
    return "".join(output)


def _contains_identifier(text: str, identifier: str) -> bool:
    marker = "__h21_identifier_probe__"
    return rename_lean_identifier(text, identifier, marker) != text


def _equation_type(equation_text: str) -> str:
    try:
        left, right, variables = parse_equation(equation_text)
    except (TypeError, ValueError) as exc:
        raise WaypointProtocolError("composition_replay_error", str(exc)) from exc
    equality = f"{render_term(left)} = {render_term(right)}"
    if not variables:
        return equality
    return "∀ ({} : G), {}".format(" ".join(variables), equality)


def compose_link_proofs(
    target_texts: Sequence[str],
    link_proofs: Sequence[LinkProof],
) -> str:
    if not target_texts or len(target_texts) != len(link_proofs):
        raise WaypointProtocolError(
            "composition_replay_error", "link target/proof cardinality drift"
        )
    lines: list[str] = []
    previous_hypothesis = "hyp"
    for index, (target_text, link) in enumerate(zip(target_texts, link_proofs)):
        if not _contains_identifier(link.proof_body, "hyp"):
            raise WaypointProtocolError(
                "composition_replay_error",
                f"link {index} proof does not reference its source hypothesis",
            )
        local_name = f"h21_link_{index}"
        renamed = rename_lean_identifier(
            link.proof_body, "hyp", previous_hypothesis
        )
        if previous_hypothesis != "hyp" and _contains_identifier(renamed, "hyp"):
            raise WaypointProtocolError(
                "composition_replay_error",
                f"link {index} source-hypothesis alpha-renaming failed",
            )
        lines.append(f"have {local_name} : {_equation_type(target_text)} := by")
        lines.extend(
            "  " + line if line.strip() else ""
            for line in renamed.strip().splitlines()
        )
        previous_hypothesis = local_name
    lines.append(f"exact {previous_hypothesis}")
    code = make_true_code("\n".join(lines))
    if len(code.encode("utf-8")) > MAX_LEAN_CODE_BYTES:
        raise WaypointProtocolError(
            "certificate_byte_cap",
            f"composed certificate exceeds {MAX_LEAN_CODE_BYTES} bytes",
        )
    return code


def _link_failure(index: int, total: int) -> str:
    if index == 0:
        return "forward_link_unproved"
    if index == total - 1:
        return "goal_link_unproved"
    return "middle_link_unproved"


def verify_plan(
    eq1_text: str,
    eq2_text: str,
    plan: BridgePlan,
    *,
    object_index: int,
    engines: Sequence[LinkEngine] = DEFAULT_LINK_ENGINES,
) -> tuple[tuple[CandidateAttempt, ...], VerifiedCandidate | None]:
    attempts: list[CandidateAttempt] = []
    for chain_index, chain in enumerate(plan.chains):
        target_texts = [item.normalized_text for item in chain.waypoints]
        target_texts.append(eq2_text)
        source_text = eq1_text
        link_proofs: list[LinkProof] = []
        failed = False
        for link_index, target_text in enumerate(target_texts):
            try:
                link = prove_link(source_text, target_text, engines=engines)
            except WaypointProtocolError as exc:
                attempts.append(
                    CandidateAttempt(
                        object_index,
                        chain_index,
                        exc.category,
                        len(link_proofs),
                    )
                )
                failed = True
                break
            if link is None:
                attempts.append(
                    CandidateAttempt(
                        object_index,
                        chain_index,
                        _link_failure(link_index, len(target_texts)),
                        len(link_proofs),
                    )
                )
                failed = True
                break
            link_proofs.append(link)
            source_text = target_text
        if failed:
            continue
        try:
            code = compose_link_proofs(target_texts, link_proofs)
        except WaypointProtocolError as exc:
            attempts.append(
                CandidateAttempt(
                    object_index,
                    chain_index,
                    exc.category,
                    len(link_proofs),
                )
            )
            continue
        engine_counts = dict(sorted(Counter(item.engine for item in link_proofs).items()))
        candidate = VerifiedCandidate(
            verdict="true",
            code=code,
            digest=sha256_bytes(code.encode("utf-8")),
            link_count=len(link_proofs),
            engine_counts=engine_counts,
        )
        attempts.append(
            CandidateAttempt(
                object_index,
                chain_index,
                "accepted",
                len(link_proofs),
            )
        )
        return tuple(attempts), candidate
    return tuple(attempts), None


def compile_response(
    eq1_text: str,
    eq2_text: str,
    response_text: Any,
    *,
    digest_history: Sequence[str] = (),
    provider_truncated: bool = False,
    engines: Sequence[LinkEngine] = DEFAULT_LINK_ENGINES,
) -> ResponseVerification:
    extraction = extract_json_objects(
        response_text, provider_truncated=provider_truncated
    )
    if extraction.error_category is not None:
        return ResponseVerification(extraction, (), None, None)
    history = set(digest_history)
    attempts: list[CandidateAttempt] = []
    latest_plan_digest: str | None = None
    for object_index, value in enumerate(extraction.objects):
        try:
            plan = parse_bridge_plan(eq1_text, eq2_text, value)
        except WaypointProtocolError as exc:
            attempts.append(
                CandidateAttempt(object_index, None, exc.category, 0)
            )
            continue
        latest_plan_digest = plan.digest
        if plan.digest in history:
            attempts.append(
                CandidateAttempt(object_index, None, "duplicate_waypoint", 0)
            )
            continue
        plan_attempts, candidate = verify_plan(
            eq1_text,
            eq2_text,
            plan,
            object_index=object_index,
            engines=engines,
        )
        attempts.extend(plan_attempts)
        if candidate is not None:
            return ResponseVerification(
                extraction,
                tuple(attempts),
                candidate,
                plan.digest,
            )
    return ResponseVerification(
        extraction,
        tuple(attempts),
        None,
        latest_plan_digest,
    )


def typed_feedback(result: ResponseVerification) -> str:
    if result.candidate is not None:
        category = "accepted"
    elif result.extraction.error_category is not None:
        category = result.extraction.error_category
    elif result.attempts:
        category = result.attempts[-1].category
    else:
        category = "schema_error"
    counts = Counter(attempt.category for attempt in result.attempts)
    payload = {
        "category": category,
        "attempt_categories": dict(sorted(counts.items())),
        "candidate_objects_examined": len(result.extraction.objects),
        "chains_examined": sum(
            attempt.chain_index is not None for attempt in result.attempts
        ),
        "detail": "typed aggregate only; propose a different bounded bridge chain",
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))

MAX_CANDIDATE_OBJECTS = 4

MINIMUM_DEADLINE_START_SLACK_SECONDS = 0.25

FAILURE_CATEGORIES = (
    "transport_error",
    "empty_response",
    "truncated_response",
    "no_json_object",
    "schema_error",
    "term_parse_error",
    "term_cap_error",
    "duplicate_waypoint",
    "degenerate_waypoint",
    "forward_link_unproved",
    "middle_link_unproved",
    "goal_link_unproved",
    "engine_timeout",
    "engine_cap_exhausted",
    "response_deadline_exhausted",
    "engine_invocation_budget_exhausted",
    "controller_internal_error",
    "composition_replay_error",
    "certificate_byte_cap",
    "lean_judge_rejection",
    "accepted",
)

FAIL_CLOSED_CATEGORIES = (
    "engine_timeout",
    "engine_cap_exhausted",
    "response_deadline_exhausted",
    "engine_invocation_budget_exhausted",
    "controller_internal_error",
)

@dataclass(frozen=True)
class CapTier:
    tier_id: str
    maximum_depth_per_engine: int
    maximum_rules_per_engine: int
    maximum_candidates_per_engine: int
    maximum_queue_per_engine: int
    maximum_term_size: int
    maximum_demodulation_rewrites_per_side: int

    def h19_globals(self) -> dict[str, int]:
        return {
            "MAX_DEPTH": self.maximum_depth_per_engine,
            "MAX_RULES": self.maximum_rules_per_engine,
            "MAX_CANDIDATES": self.maximum_candidates_per_engine,
            "MAX_QUEUE": self.maximum_queue_per_engine,
            "MAX_TERM_SIZE": self.maximum_term_size,
            "MAX_DEMODULATION_REWRITES_PER_SIDE": (
                self.maximum_demodulation_rewrites_per_side
            ),
        }


CAP_TIERS = {
    "compact": CapTier("compact", 12, 512, 2_048, 32_768, 45, 4),
    "balanced": CapTier("balanced", 15, 1_024, 4_096, 65_536, 45, 6),
    "legacy_ceiling": CapTier(
        "legacy_ceiling", 18, 2_048, 8_192, 131_072, 45, 8
    ),
}


@dataclass(frozen=True)
class ControllerVariant:
    variant_id: str
    cap_tier: str
    engine_invocation_maximum: int
    engine_wall_seconds: float
    response_wall_seconds: float

    def __post_init__(self) -> None:
        if self.cap_tier not in CAP_TIERS:
            raise ValueError(f"unknown H22 cap tier: {self.cap_tier}")
        if self.engine_invocation_maximum < 1:
            raise ValueError("engine invocation maximum must be positive")
        if self.engine_wall_seconds <= 0 or self.response_wall_seconds <= 0:
            raise ValueError("H22 wall-time limits must be positive")

    @property
    def tier(self) -> CapTier:
        return CAP_TIERS[self.cap_tier]


ORDERED_ADMISSIBLE_VARIANTS = (
    ControllerVariant("compact_tight", "compact", 12, 8.0, 45.0),
    ControllerVariant("compact_balanced", "compact", 16, 15.0, 75.0),
    ControllerVariant("balanced_tight", "balanced", 12, 8.0, 45.0),
    ControllerVariant("compact_guarded", "compact", 20, 25.0, 105.0),
    ControllerVariant("balanced_balanced", "balanced", 16, 15.0, 75.0),
    ControllerVariant("legacy_tight", "legacy_ceiling", 12, 8.0, 45.0),
    ControllerVariant("balanced_guarded", "balanced", 20, 25.0, 105.0),
    ControllerVariant("legacy_balanced", "legacy_ceiling", 16, 15.0, 75.0),
    ControllerVariant("legacy_guarded", "legacy_ceiling", 20, 25.0, 105.0),
)


class EngineCapExhausted(RuntimeError):
    """Explicit engine signal that a declared work cap was reached."""


class _HardEngineTimeout(TimeoutError):
    pass


@dataclass(frozen=True)
class EngineBinding:
    name: str
    function: Callable[[str, str], Any]
    uses_frozen_h19_caps: bool = False


DEFAULT_ENGINES = (
    EngineBinding(
        "expanded_goal_paramodulation",
        expanded_cap_proof,
        True,
    ),
    EngineBinding(
        "demodulating_goal_paramodulation",
        demodulating_goal_paramodulation_proof,
        True,
    ),
)


@dataclass(frozen=True)
class LinkResolution:
    proof: Any | None
    category: str | None


@dataclass(frozen=True)
class ControllerMetrics:
    engine_invocations: int
    cache_hits: int
    engine_invocation_counts: dict[str, int]


@dataclass(frozen=True)
class BudgetedResponseVerification:
    extraction: Any
    attempts: tuple[Any, ...]
    candidate: Any | None
    plan_digest: str | None
    metrics: ControllerMetrics


_H19_CAP_LOCK = threading.RLock()


@contextmanager
def _temporary_h19_caps(tier: CapTier) -> Iterator[None]:
    desired = tier.h19_globals()
    with _H19_CAP_LOCK:
        previous = {name: globals()[name] for name in desired}
        try:
            for name, value in desired.items():
                globals()[name] = value
            yield
        finally:
            for name, value in previous.items():
                globals()[name] = value


def _hard_posix_call(function: Callable[[], Any], timeout_seconds: float) -> Any:
    """Run ``function`` under ITIMER_REAL and restore prior signal state."""
    if timeout_seconds <= 0:
        raise _HardEngineTimeout("engine deadline already exhausted")
    if threading.current_thread() is not threading.main_thread():
        raise RuntimeError("POSIX engine timer requires the main thread")

    previous_handler = signal.getsignal(signal.SIGALRM)
    previous_delay, previous_interval = signal.getitimer(signal.ITIMER_REAL)
    started = time.monotonic()

    def interrupt(_signum: int, _frame: Any) -> None:
        raise _HardEngineTimeout("H22 engine wall-time limit reached")

    signal.signal(signal.SIGALRM, interrupt)
    signal.setitimer(signal.ITIMER_REAL, timeout_seconds)
    try:
        return function()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        signal.signal(signal.SIGALRM, previous_handler)
        if previous_delay > 0.0:
            elapsed = time.monotonic() - started
            remaining = max(previous_delay - elapsed, 1e-6)
            signal.setitimer(
                signal.ITIMER_REAL,
                remaining,
                previous_interval,
            )


def _coerce_engines(
    engines: Sequence[EngineBinding | tuple[str, Callable[[str, str], Any]]],
) -> tuple[EngineBinding, ...]:
    output: list[EngineBinding] = []
    for value in engines:
        if isinstance(value, EngineBinding):
            output.append(value)
            continue
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("H22 engine bindings must be EngineBinding or pairs")
        name, function = value
        if not isinstance(name, str) or not callable(function):
            raise TypeError("invalid H22 engine pair")
        output.append(EngineBinding(name, function, False))
    if not output:
        raise ValueError("at least one H22 engine binding is required")
    return tuple(output)


def _canonical_link_key(source_text: str, target_text: str) -> tuple[Any, Any]:
    return (
        canonical_equation(source_text),
        canonical_equation(target_text),
    )


@dataclass
class BudgetController:
    variant: ControllerVariant
    engines: Sequence[
        EngineBinding | tuple[str, Callable[[str, str], Any]]
    ] = DEFAULT_ENGINES
    _started: float = field(init=False, repr=False)
    _deadline: float = field(init=False, repr=False)
    _engine_invocations: int = field(default=0, init=False, repr=False)
    _cache_hits: int = field(default=0, init=False, repr=False)
    _engine_counts: Counter[str] = field(
        default_factory=Counter, init=False, repr=False
    )
    _cache: dict[tuple[Any, Any], LinkResolution] = field(
        default_factory=dict, init=False, repr=False
    )

    def __post_init__(self) -> None:
        self.engines = _coerce_engines(self.engines)
        self._started = time.monotonic()
        self._deadline = self._started + self.variant.response_wall_seconds

    def metrics(self) -> ControllerMetrics:
        return ControllerMetrics(
            self._engine_invocations,
            self._cache_hits,
            dict(sorted(self._engine_counts.items())),
        )

    def _remaining(self) -> float:
        return self._deadline - time.monotonic()

    def _cache_resolution(
        self, key: tuple[Any, Any], resolution: LinkResolution
    ) -> LinkResolution:
        self._cache[key] = resolution
        return resolution

    def resolve_link(self, source_text: str, target_text: str) -> LinkResolution:
        try:
            key = _canonical_link_key(source_text, target_text)
        except Exception:
            return LinkResolution(None, "controller_internal_error")
        if key in self._cache:
            self._cache_hits += 1
            return self._cache[key]

        saw_no_candidate = False
        for engine in self.engines:
            remaining = self._remaining()
            if remaining < MINIMUM_DEADLINE_START_SLACK_SECONDS:
                return self._cache_resolution(
                    key, LinkResolution(None, "response_deadline_exhausted")
                )
            if self._engine_invocations >= self.variant.engine_invocation_maximum:
                return self._cache_resolution(
                    key,
                    LinkResolution(
                        None, "engine_invocation_budget_exhausted"
                    ),
                )
            self._engine_invocations += 1
            self._engine_counts[engine.name] += 1
            timeout_seconds = min(
                self.variant.engine_wall_seconds,
                remaining,
            )

            def invoke() -> Any:
                if engine.uses_frozen_h19_caps:
                    with _temporary_h19_caps(self.variant.tier):
                        return engine.function(source_text, target_text)
                return engine.function(source_text, target_text)

            try:
                proof = _hard_posix_call(invoke, timeout_seconds)
            except _HardEngineTimeout:
                return self._cache_resolution(
                    key, LinkResolution(None, "engine_timeout")
                )
            except EngineCapExhausted:
                return self._cache_resolution(
                    key, LinkResolution(None, "engine_cap_exhausted")
                )
            except Exception:
                return self._cache_resolution(
                    key, LinkResolution(None, "controller_internal_error")
                )

            if self._remaining() < 0.0:
                return self._cache_resolution(
                    key, LinkResolution(None, "response_deadline_exhausted")
                )
            if proof is None:
                saw_no_candidate = True
                continue
            if not isinstance(proof, str) or not proof.strip():
                return self._cache_resolution(
                    key, LinkResolution(None, "composition_replay_error")
                )
            return self._cache_resolution(
                key,
                LinkResolution(LinkProof(engine.name, proof), None),
            )

        if saw_no_candidate:
            return self._cache_resolution(key, LinkResolution(None, None))
        return self._cache_resolution(
            key, LinkResolution(None, "controller_internal_error")
        )


def _link_failure(index: int, total: int) -> str:
    if index == 0:
        return "forward_link_unproved"
    if index == total - 1:
        return "goal_link_unproved"
    return "middle_link_unproved"


def _verify_plan(
    eq1_text: str,
    eq2_text: str,
    plan: Any,
    *,
    object_index: int,
    controller: BudgetController,
) -> tuple[tuple[Any, ...], Any | None, bool]:
    attempts: list[Any] = []
    for chain_index, chain in enumerate(plan.chains):
        target_texts = [item.normalized_text for item in chain.waypoints]
        target_texts.append(eq2_text)
        source_text = eq1_text
        link_proofs: list[Any] = []
        failed = False
        for link_index, target_text in enumerate(target_texts):
            resolution = controller.resolve_link(source_text, target_text)
            if resolution.category is not None:
                attempts.append(
                    CandidateAttempt(
                        object_index,
                        chain_index,
                        resolution.category,
                        len(link_proofs),
                    )
                )
                if resolution.category in FAIL_CLOSED_CATEGORIES:
                    return tuple(attempts), None, True
                failed = True
                break
            if resolution.proof is None:
                attempts.append(
                    CandidateAttempt(
                        object_index,
                        chain_index,
                        _link_failure(link_index, len(target_texts)),
                        len(link_proofs),
                    )
                )
                failed = True
                break
            link_proofs.append(resolution.proof)
            source_text = target_text
        if failed:
            continue
        try:
            code = compose_link_proofs(target_texts, link_proofs)
        except WaypointProtocolError as exc:
            attempts.append(
                CandidateAttempt(
                    object_index,
                    chain_index,
                    exc.category,
                    len(link_proofs),
                )
            )
            continue
        engine_counts = dict(
            sorted(Counter(item.engine for item in link_proofs).items())
        )
        candidate = VerifiedCandidate(
            verdict="true",
            code=code,
            digest=sha256_bytes(code.encode("utf-8")),
            link_count=len(link_proofs),
            engine_counts=engine_counts,
        )
        attempts.append(
            CandidateAttempt(
                object_index,
                chain_index,
                "accepted",
                len(link_proofs),
            )
        )
        return tuple(attempts), candidate, False
    return tuple(attempts), None, False


def compile_response(
    eq1_text: str,
    eq2_text: str,
    response_text: Any,
    *,
    variant: ControllerVariant,
    digest_history: Sequence[str] = (),
    provider_truncated: bool = False,
    engines: Sequence[
        EngineBinding | tuple[str, Callable[[str, str], Any]]
    ] = DEFAULT_ENGINES,
) -> BudgetedResponseVerification:
    controller = BudgetController(variant, engines)
    extraction = extract_json_objects(
        response_text,
        provider_truncated=provider_truncated,
        maximum_objects=MAX_CANDIDATE_OBJECTS,
    )
    if extraction.error_category is not None:
        return BudgetedResponseVerification(
            extraction, (), None, None, controller.metrics()
        )
    history = set(digest_history)
    attempts: list[Any] = []
    latest_plan_digest: str | None = None
    for object_index, value in enumerate(extraction.objects):
        try:
            plan = parse_bridge_plan(eq1_text, eq2_text, value)
        except WaypointProtocolError as exc:
            attempts.append(
                CandidateAttempt(object_index, None, exc.category, 0)
            )
            continue
        latest_plan_digest = plan.digest
        if plan.digest in history:
            attempts.append(
                CandidateAttempt(
                    object_index, None, "duplicate_waypoint", 0
                )
            )
            continue
        plan_attempts, candidate, terminal = _verify_plan(
            eq1_text,
            eq2_text,
            plan,
            object_index=object_index,
            controller=controller,
        )
        attempts.extend(plan_attempts)
        if candidate is not None:
            return BudgetedResponseVerification(
                extraction,
                tuple(attempts),
                candidate,
                plan.digest,
                controller.metrics(),
            )
        if terminal:
            break
    return BudgetedResponseVerification(
        extraction,
        tuple(attempts),
        None,
        latest_plan_digest,
        controller.metrics(),
    )


def result_category(result: BudgetedResponseVerification) -> str:
    if result.candidate is not None:
        return "accepted"
    if result.extraction.error_category is not None:
        return str(result.extraction.error_category)
    if result.attempts:
        return str(result.attempts[-1].category)
    return "schema_error"


def typed_feedback(result: BudgetedResponseVerification) -> str:
    counts = Counter(attempt.category for attempt in result.attempts)
    payload = {
        "category": result_category(result),
        "attempt_categories": dict(sorted(counts.items())),
        "candidate_objects_examined": len(result.extraction.objects),
        "chains_examined": sum(
            attempt.chain_index is not None for attempt in result.attempts
        ),
        "controller": {
            "cache_hits": result.metrics.cache_hits,
            "engine_invocation_counts": result.metrics.engine_invocation_counts,
            "engine_invocations": result.metrics.engine_invocations,
        },
        "detail": (
            "typed aggregate only; propose a different bounded bridge chain"
        ),
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def controller_contract_payload() -> dict[str, Any]:
    return {
        "candidate_objects_examined_maximum": MAX_CANDIDATE_OBJECTS,
        "engine_order_per_link": [engine.name for engine in DEFAULT_ENGINES],
        "fail_closed_categories": list(FAIL_CLOSED_CATEGORIES),
        "minimum_deadline_start_slack_seconds": (
            MINIMUM_DEADLINE_START_SLACK_SECONDS
        ),
        "cap_tiers": [
            {
                "tier_id": tier.tier_id,
                "maximum_depth_per_engine": tier.maximum_depth_per_engine,
                "maximum_rules_per_engine": tier.maximum_rules_per_engine,
                "maximum_candidates_per_engine": (
                    tier.maximum_candidates_per_engine
                ),
                "maximum_queue_per_engine": tier.maximum_queue_per_engine,
                "maximum_term_size": tier.maximum_term_size,
                "maximum_demodulation_rewrites_per_side": (
                    tier.maximum_demodulation_rewrites_per_side
                ),
            }
            for tier in CAP_TIERS.values()
        ],
        "ordered_admissible_variants": [
            {
                "variant_id": value.variant_id,
                "cap_tier": value.cap_tier,
                "engine_invocation_maximum": (
                    value.engine_invocation_maximum
                ),
                "engine_wall_seconds": value.engine_wall_seconds,
                "response_wall_seconds": value.response_wall_seconds,
            }
            for value in ORDERED_ADMISSIBLE_VARIANTS
        ],
    }

MAX_LLM_ROUNDS = 3

MAX_TRACE_CHARACTERS = 12_000

MAX_JUDGE_STATUS_CHARACTERS = 80

SELECTED_VARIANT_ID = "compact_tight"

SELECTED_CAP_TIER = "compact"

SELECTED_ENGINE_INVOCATION_MAXIMUM = 12

SELECTED_ENGINE_WALL_SECONDS = 8.0

SELECTED_RESPONSE_WALL_SECONDS = 45.0

SELECTED_VARIANT = ORDERED_ADMISSIBLE_VARIANTS[0]

def _trace_summary(trace) -> str:
    sanitized = []
    for item in trace:
        text = re.sub(r"\s+", " ", str(item)).strip()
        if " -> " in text:
            lane, outcome = text.split(" -> ", 1)
            lane = re.sub(r"[^a-zA-Z0-9_.: -]+", "_", lane)[:160]
            lowered = outcome.lower()
            category = "recorded"
            for prefix, replacement in (
                ("accepted", "accepted"),
                ("rejected", "rejected"),
                ("invalid", "invalid"),
                ("no candidate", "no_candidate"),
                ("duplicate", "duplicate"),
                ("structural gate miss", "structural_gate_miss"),
                ("certificate exceeds", "certificate_byte_cap"),
                ("transport", "transport_error"),
            ):
                if lowered.startswith(prefix):
                    category = replacement
                    break
            sanitized.append(f"{lane} -> {category}")
        elif text.startswith("strategy order:"):
            sanitized.append(re.sub(r"[^a-zA-Z0-9_.: >-]+", "_", text)[:600])
        else:
            sanitized.append("deterministic_event_recorded")
    text = "\n".join(sanitized)
    if len(text) <= MAX_TRACE_CHARACTERS:
        return text
    return "... [earlier deterministic trace truncated]\n" + text[-MAX_TRACE_CHARACTERS:]


def _feedback_category(feedback_json: str) -> str:
    try:
        value = json.loads(feedback_json)
    except (TypeError, ValueError):
        return "schema_error"
    category = value.get("category") if isinstance(value, dict) else None
    return category if category in FAILURE_CATEGORIES else "schema_error"


def _protocol_mode(round_number: int, feedback_json: str) -> str:
    if round_number == 0:
        return "compact_budget_easiest_locally_provable_bridge_first"
    return "compact_budget_structural_repair:" + _feedback_category(feedback_json)


def _judge_status(response) -> str:
    status = response.get("status", "unknown") if isinstance(response, dict) else "invalid"
    status = re.sub(r"[^a-zA-Z0-9_.:-]+", "_", str(status)).strip("_")
    return (status or "unknown")[:MAX_JUDGE_STATUS_CHARACTERS]


def _judge_rejection_feedback(response) -> str:
    return json.dumps(
        {
            "category": "lean_judge_rejection",
            "detail": "locally composed certificate was rejected; propose a structurally different bridge plan",
            "judge_status": _judge_status(response),
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _attempt_counts(verification) -> dict[str, int]:
    counts: dict[str, int] = {}
    for attempt in verification.attempts:
        counts[attempt.category] = counts.get(attempt.category, 0) + 1
    return dict(sorted(counts.items()))


def _h22_budgeted_waypoint_fallback(problem, eq1_text, eq2_text, trace, feedback):
    del problem  # Problem identity and labels are never exposed to this lane.
    plan_digest_history: list[str] = []
    protocol_feedback = json.dumps(
        {
            "category": "none",
            "detail": "first bounded bridge-plan attempt",
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    for round_number in range(MAX_LLM_ROUNDS):
        context = {
            "round": str(round_number + 1),
            "mode": _protocol_mode(round_number, protocol_feedback),
            "deterministic_trace_summary": _trace_summary(trace),
            "protocol_feedback": protocol_feedback,
            "tried_plan_count": str(len(plan_digest_history)),
        }
        log_event(
            "llm_request",
            round=round_number,
            route="organizer_proxy",
            protocol="h22_budgeted_waypoint_verifier_v1",
        )
        response = call_llm(context)
        if not isinstance(response, dict) or "error" in response:
            trace.append(f"h22 waypoint round {round_number} -> transport_error")
            log_event(
                "llm_unavailable",
                round=round_number,
                category="transport_error",
            )
            return False
        verification = compile_response(
            eq1_text,
            eq2_text,
            response.get("response", ""),
            variant=SELECTED_VARIANT,
            digest_history=plan_digest_history,
            provider_truncated=bool(response.get("truncated")),
        )
        if (
            verification.plan_digest is not None
            and verification.plan_digest not in plan_digest_history
        ):
            plan_digest_history.append(verification.plan_digest)
        protocol_feedback = typed_feedback(verification)
        category = _feedback_category(protocol_feedback)
        trace.append(f"h22 waypoint round {round_number} -> {category}")
        log_event(
            "waypoint_response_checked",
            round=round_number,
            category=category,
            candidate_objects_examined=len(verification.extraction.objects),
            chains_examined=sum(
                attempt.chain_index is not None for attempt in verification.attempts
            ),
            attempt_categories=_attempt_counts(verification),
            plan_count=len(plan_digest_history),
            controller_engine_invocations=(
                verification.metrics.engine_invocations
            ),
            controller_cache_hits=verification.metrics.cache_hits,
            controller_engine_invocation_counts=(
                verification.metrics.engine_invocation_counts
            ),
            controller_variant=SELECTED_VARIANT_ID,
        )
        candidate = verification.candidate
        if candidate is None:
            continue
        log_event(
            "candidate",
            strategy=f"h22_budgeted_waypoint_round_{round_number}",
            verdict="true",
            code_bytes=len(candidate.code.encode("utf-8")),
            link_count=candidate.link_count,
            engine_counts=candidate.engine_counts,
        )
        judge = call_judge("true", candidate.code)
        status = _judge_status(judge)
        feedback.append(status)
        trace.append(f"h22 budgeted waypoint round {round_number} -> {status}")
        log_event(
            "judge_result",
            strategy=f"h22_budgeted_waypoint_round_{round_number}",
            status=status,
        )
        if isinstance(judge, dict) and judge.get("status") == "accepted":
            return True
        protocol_feedback = _judge_rejection_feedback(judge)
    return False

if (
    SELECTED_VARIANT.variant_id,
    SELECTED_VARIANT.cap_tier,
    SELECTED_VARIANT.engine_invocation_maximum,
    SELECTED_VARIANT.engine_wall_seconds,
    SELECTED_VARIANT.response_wall_seconds,
) != (
    SELECTED_VARIANT_ID,
    SELECTED_CAP_TIER,
    SELECTED_ENGINE_INVOCATION_MAXIMUM,
    SELECTED_ENGINE_WALL_SECONDS,
    SELECTED_RESPONSE_WALL_SECONDS,
):
    raise RuntimeError("frozen H22 compact_tight selection drift")

_ORIGINAL_LLM_FALLBACK = _h22_budgeted_waypoint_fallback

# H43 research-only current-contract H22 Marathon adapter. Every emitted
# certificate is independently compiled before append and is formally judged
# again by the official Marathon scorer. Model output is untrusted advice only.
import io as _h43_io
import os as _h43_os
from pathlib import Path as _H43Path
import signal as _h43_signal
import subprocess as _h43_subprocess
import sys as _h43_sys
import time as _h43_time

H43_LLM_CONFIG = {
    "model": "openai/gpt-oss-120b",
    "provider": "deepinfra/bf16",
    "reasoning_effort": "low",
    "temperature": 0.0,
    "seed": 0,
    "max_output_tokens": 16384,
}
H43_TAIL_RESERVE_SECONDS = 30.0
H43_DETERMINISTIC_ROW_SECONDS = 45.0
H43_VERIFIER_RESERVE_SECONDS = 45.0


class _H43RowTimeout(Exception):
    pass


def _h43_alarm(_signum, _frame):
    raise _H43RowTimeout("frozen deterministic per-row deadline")


def _h43_equation_def(name, text):
    text = normalize_operator(text)
    if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", name):
        raise ValueError("invalid equation definition name")
    if not isinstance(text, str) or not re.fullmatch(r"[\sa-zA-Z0-9◇=()]+", text):
        raise ValueError("invalid equation text")
    depth = 0
    for character in text:
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth < 0:
                raise ValueError("unbalanced equation text")
    if depth != 0:
        raise ValueError("unbalanced equation text")
    variables = []
    for variable in re.findall(r"\b([a-z])\b", text):
        if variable not in variables:
            variables.append(variable)
    binders = " ".join("(%s : G)" % variable for variable in variables)
    return "@[reducible] def %s (G : Type _) [Magma G] : Prop := ∀ %s, %s" % (
        name,
        binders,
        text,
    )


def _h43_compile_candidate(problem, verdict, code, remaining_seconds, scratch_dir, ordinal):
    if verdict not in ("true", "false"):
        return False
    if not isinstance(code, str):
        return False
    payload = code.encode("utf-8", errors="strict")
    if not payload or len(payload) > 100000:
        return False
    lean_bin = _h43_os.environ.get("JUDGE_LEAN_BIN") or "lean"
    artifact_dir = scratch_dir / ("verify_%04d" % ordinal)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    problem_source = artifact_dir / "JudgeProblem.lean"
    problem_olean = artifact_dir / "JudgeProblem.olean"
    source = artifact_dir / "Submission.lean"
    try:
        equation1 = problem["equation1"]
        equation2 = problem["equation2"]
        goal = (
            "∀ (G : Type) [Magma G], EquationLHS G → EquationRHS G"
            if verdict == "true"
            else "∃ (G : Type) (_ : Magma G), EquationLHS G ∧ ¬ EquationRHS G"
        )
        problem_source.write_text(
            "import JudgeMagma.Magma\n\n"
            + _h43_equation_def("EquationLHS", equation1)
            + "\n"
            + _h43_equation_def("EquationRHS", equation2)
            + "\n\nabbrev Goal : Prop := " + goal + "\n",
            encoding="utf-8",
        )
        source.write_bytes(payload)
    except (KeyError, OSError, TypeError, UnicodeError, ValueError):
        return False
    environment = _h43_os.environ.copy()
    environment["LEAN_PATH"] = str(artifact_dir)
    verify_deadline = _h43_time.monotonic() + max(
        1.0, min(float(remaining_seconds), H43_VERIFIER_RESERVE_SECONDS)
    )
    try:
        problem_compile = _h43_subprocess.run(
            [lean_bin, "--root=" + str(artifact_dir), "-o", str(problem_olean), str(problem_source)],
            cwd=str(artifact_dir),
            env=environment,
            stdin=_h43_subprocess.DEVNULL,
            stdout=_h43_subprocess.DEVNULL,
            stderr=_h43_subprocess.DEVNULL,
            timeout=max(1.0, verify_deadline - _h43_time.monotonic()),
            check=False,
        )
        if problem_compile.returncode != 0:
            return False
        remaining_seconds = verify_deadline - _h43_time.monotonic()
        if remaining_seconds <= 1.0:
            return False
        submission_compile = _h43_subprocess.run(
            [lean_bin, "--root=" + str(artifact_dir), str(source)],
            cwd=str(artifact_dir),
            env=environment,
            stdin=_h43_subprocess.DEVNULL,
            stdout=_h43_subprocess.DEVNULL,
            stderr=_h43_subprocess.DEVNULL,
            timeout=remaining_seconds,
            check=False,
        )
        return submission_compile.returncode == 0
    except (OSError, _h43_subprocess.SubprocessError, ValueError):
        return False
    finally:
        try:
            source.unlink()
        except OSError:
            pass


def _h43_solve_problem(problem, deadline, scratch_dir, ordinal):
    captured = []
    original_stdin = _h43_sys.stdin
    original_call_judge = globals()["call_judge"]
    original_call_llm = globals()["call_llm"]

    def local_judge(verdict, code):
        remaining = deadline - _h43_time.monotonic()
        accepted = remaining > 1.0 and _h43_compile_candidate(
            problem, verdict, code, remaining, scratch_dir, ordinal
        )
        if accepted and not captured:
            captured.append({"verdict": verdict, "code": code})
        return {"status": "accepted" if accepted else "incorrect"}

    def local_llm(context):
        remaining = deadline - _h43_time.monotonic() - H43_TAIL_RESERVE_SECONDS
        if remaining <= H43_VERIFIER_RESERVE_SECONDS + 1.0:
            return {"error": "frozen H43 wall budget exhausted"}
        try:
            cap = int(_h43_os.environ.get("JUDGE_MARATHON_BUDGET_TOKENS", "0"))
        except ValueError:
            cap = 0
        if cap <= 0:
            return {"error": "token budget is zero"}
        library = _h43_os.environ.get("JUDGE_MARATHON_LIB_DIR")
        if not library:
            return {"error": "official Marathon helper unavailable"}
        if library not in _h43_sys.path:
            _h43_sys.path.insert(0, library)
        try:
            from marathon_llm import call_llm as helper
            return helper(
                str(context),
                config=H43_LLM_CONFIG,
                max_seconds=max(1.0, remaining - H43_VERIFIER_RESERVE_SECONDS),
            )
        except Exception:
            return {"error": "official Marathon helper failed closed"}

    try:
        globals()["call_judge"] = local_judge
        globals()["call_llm"] = local_llm
        _h43_sys.stdin = _h43_io.StringIO(
            json.dumps({"problem": problem}, separators=(",", ":")) + "\n"
        )
        old_handler = None
        if hasattr(_h43_signal, "SIGALRM"):
            old_handler = _h43_signal.signal(_h43_signal.SIGALRM, _h43_alarm)
            _h43_signal.setitimer(
                _h43_signal.ITIMER_REAL,
                max(0.001, min(H43_DETERMINISTIC_ROW_SECONDS, deadline - _h43_time.monotonic())),
            )
        try:
            _H43_SOLO_MAIN()
        except (_H43RowTimeout, EOFError, SystemExit, Exception):
            pass
        finally:
            if hasattr(_h43_signal, "SIGALRM"):
                _h43_signal.setitimer(_h43_signal.ITIMER_REAL, 0.0)
                if old_handler is not None:
                    _h43_signal.signal(_h43_signal.SIGALRM, old_handler)
    finally:
        _h43_sys.stdin = original_stdin
        globals()["call_judge"] = original_call_judge
        globals()["call_llm"] = original_call_llm
    return captured[0] if captured else None


def _h43_marathon_main():
    manifest = _H43Path(_h43_os.environ["JUDGE_MARATHON_MANIFEST"])
    output = _H43Path(_h43_os.environ["JUDGE_MARATHON_OUTPUT"])
    scratch_dir = _H43Path(
        _h43_os.environ.get("JUDGE_MARATHON_SCRATCH_DIR", str(output.parent))
    )
    scratch_dir.mkdir(parents=True, exist_ok=True)
    try:
        total_budget = float(_h43_os.environ.get("JUDGE_MARATHON_BUDGET_SECONDS", "0"))
    except ValueError:
        total_budget = 0.0
    deadline = _h43_time.monotonic() + max(0.0, total_budget)
    with manifest.open("r", encoding="utf-8") as source:
        for ordinal, line in enumerate(source, start=1):
            if deadline - _h43_time.monotonic() <= H43_TAIL_RESERVE_SECONDS:
                break
            try:
                problem = json.loads(line)
                problem_id = problem["id"]
                if not isinstance(problem_id, str):
                    continue
            except (KeyError, TypeError, ValueError):
                continue
            result = _h43_solve_problem(problem, deadline, scratch_dir, ordinal)
            if result is None:
                continue
            record = {"id": problem_id, "verdict": result["verdict"], "code": result["code"]}
            with output.open("a", encoding="utf-8") as sink:
                sink.write(json.dumps(record, separators=(",", ":")) + "\n")
                sink.flush()


_H43_SOLO_MAIN = main


def main():
    if _h43_os.environ.get("JUDGE_MARATHON_MANIFEST"):
        return _h43_marathon_main()
    return _H43_SOLO_MAIN()


if __name__ == "__main__":
    main()
