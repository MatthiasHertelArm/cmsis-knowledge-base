---
id: "alp-training-inference-pytorch-fine-tune-2-running-the-script"
type: "concept"
domain: "edge-ai"
title: "Edge AI on Arm: PyTorch and ExecuTorch rock-paper-scissors: Train and Test the rock-paper-scissors Model: Running the Script:"
summary: "Train the model, export it, and play the game:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fine-tune-2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/training-inference-pytorch/fine-tune-2/#running-the-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

Train the model, export it, and play the game:

```bash
python rps_tiny.py --epochs 8 --export --play
```

You’ll see training progress similar to:

```output
== Building synthetic datasets ==
Train size: 3000  |  Val size: 600
  totl += float(loss)*x.size(0)
Epoch 01/8 | train 80.03% | val 98.67%
  ↑ saved rps_best.pt (val 98.67%)
Epoch 02/8 | train 99.57% | val 100.00%
  ↑ saved rps_best.pt (val 100.00%)
Epoch 03/8 | train 99.83% | val 99.83%
Epoch 08/8 | train 100.00% | val 100.00%
Training done.
Loaded weights from rps_best.pt
[export] wrote rps_tiny.pte
```

After training and export, the game starts. Type rock, paper, or scissors, and review the model’s predictions for you and a random opponent:

```output
=== Rock–Paper–Scissors: Play vs Tiny CNN ===
Type one of: rock / paper / scissors / quit

Your move> rock

You played: rock





       .=##*++=-:.
       :**-:-=++**+:
      .=#+.     :+#=.
      :*%%#*++==+**-.
      -*+::-+#%*+-.
     :+*-.   -*+-
     -*+:     -**:
      ..      .=*+.
               .::.
Model thinks you played: rock (100.0%)

Opponent played (hidden):





        ..:--*###**-
        -#**--. .:+#*.  .
        .+#-       +#+
         -*+.     :+#-
         .+#+=**###+-.  .
          -##=:.   .
    .     .+*:
          .-**
  .        :==
Model thinks opponent played: paper (100.0%)

😅 You lose!
--------------------------------------------------
Your move> paper

You played: paper





        .--:.
       .=*+++***+=:
       :++.     :+*-
       -+-      .-+-
      .=*-..   .=+=.
      :**+++**+++-
      -*-
     .++:
     :+-
Model thinks you played: paper (100.0%)

Opponent played (hidden):


                   .


         .:::::-:::.
        .+*=======+*=
        .**.       +*-     .
 .      .=+.      :++:
        .=*#*###**+=:
        .=+-   :=+-.
        .=*:    .-+=:
    .    -#-.     :=*=
         :*:       .-+-
Model thinks opponent played: rock (100.0%)

🎉 You win!
--------------------------------------------------
Your move>
```

Type `quit` to exit the game. In the next chapter, you'll prepare the model to run on the FVP.
