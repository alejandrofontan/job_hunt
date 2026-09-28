# Orbifold AI — First Interview Prep

Sep 28, 2026 · @Alejandro

First interview for the 3D reconstruction research role: owning the multi-view 4D reconstruction stack that produces Orbifold's labels (object pose, hand and body pose, tracking, contact).

## What they actually care about

The whole posting reduces to one idea: **their labels have to be provably correct**. Everything else — rigs, calibration, critics, golden datasets — serves that. Frame every answer around accuracy, measurement, and knowing when data is wrong.

- They "index on the quality of the work rather than years served" — lead with papers and repos, not titles.
- "Founding scope" and "hold that line when a deadline argues otherwise" — they want ownership and judgment, not just technical depth.

## Your fit, in plain language

"I've spent my career on the question of how accurate a 3D estimate really is, and how to tell when it's wrong. I build SLAM and reconstruction systems on real capture rigs — underwater stereo rigs, a DLR multicopter, rover datasets — and I've built the benchmarks the community uses to measure them. Your problem is the same one: get geometry right from multiple synchronized cameras, and prove it."

- **Benchmark you authored (nice-to-have, direct hit)** → VSLAM-LAB (550+ stars, 13+ baselines, 38+ datasets, one-command reproducible evaluation) and Event-LAB (ICRA 26).
- **Automated critics / catching failure before a customer does** →
  - *Forward Prediction of Target Localization Failure* (RA-L 24): predicting when localization will fail.
  - *Look Ma, No Ground Truth!*: tuning SfM/SLAM without ground truth — quality signals when labels aren't available.
  - Self-supervised DROID-SLAM fine-tuning: an image-perturbation sensitivity signal that correlates with true ATE, i.e. a label-free error estimate.
- **Real capture rigs and how they fail** → Bommie Toolkit: stereo rig calibration with Kalibr, refraction correction for underwater capture, video → COLMAP SfM with SAM masking, 3DGS reconstruction. Have concrete failure stories ready (bad extrinsics, refraction, motion blur, lighting, desync).
- **Multi-view geometry and uncertainty** → *A Model for Multi-View Residual Covariances based on Perspective Deformation* (RA-L 22); *Adaptive Outlier Thresholding for Bundle Adjustment* (ICRA 24).
- **Tracking of moving objects** → *DOT: Dynamic Object Tracking for Visual SLAM* (ICRA 21, 133 citations).
- **Long-horizon / multi-session** → *Long-Term Multi-Session 3D Reconstruction Under Substantial Appearance Change* (arXiv 26); long-term relocalization of dynamic underwater environments (IROS 25).
- **Neural reconstruction** → 3DGS in Bommie; associate supervisor on a PhD in Gaussian Splatting reconstruction (Krishnan Harikumar).
- **PyTorch** → DROID-SLAM fine-tuning (ConvGRU, differentiable SE(3) bundle adjustment layer).
- **First-author track record** → CVPR 20 oral, RSS 24, RA-L 22/23, BMVC 23, ICRA 24, IROS 25; 406 citations, h-index 9.

## Where you'll likely get pushed — and how to frame it

- **Hand / body pose, 6-DoF object pose, contact detection.** No direct publications. Be upfront, then bridge: these are multi-view geometry and tracking problems with an articulated or rigid model in the loop. Occlusion across synchronized views, bundle-adjustment-style refinement, and uncertainty on residuals are the same machinery. DOT (tracking dynamic objects inside SLAM) is the closest existing work.
- **Ray at scale.** Be honest. Point to VSLAM-LAB orchestrating many baselines × datasets reproducibly with Pixi as evidence you think about pipelines at scale; Ray is a tool to pick up.
- **Tactile / force sensing.** Not your background; your sensor-fusion experience is visual-inertial (Wikitude VIO, MADMAX dataset, factor graphs in the SLAM course).
- **Startup / fast-paced applied research.** Wikitude (industry AR SDK for mobile) plus shipping open-source tools used by others. Emphasise high agency: VSLAM-LAB and the workshops you've organized (RSS 25/26, ICRA 26) were self-initiated.
- **How label quality propagates downstream.** Have a view ready: small systematic errors (calibration drift, sync offset) are worse than random noise because the model learns them; this is why you'd prioritise critics for systematic error first.

## Questions to ask them

- What reconstruction accuracy are you hitting today, how is it measured, and which failure mode currently dominates the error budget?
- What does the capture setup look like — number of views, sync method, calibration procedure, how often rigs are recalibrated?
- How are the golden datasets (mocap, gloves, force sensing) used today — only for evaluation, or also for training?
- Who would I work with day to day, and how big is the research team right now?
- How do partner audits of labels work in practice?
- Location, visa sponsorship, and remote flexibility — and what the interview process looks like from here.
