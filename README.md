# Poker with Reinforcement Learning Agents

#### **Overview**
I created a simplified Texas Hold'em environmnet for training reinforcement learning agents using Deep Counterfactual Regret Minimization (CFR).  Additionally, [nn-holdem](https://github.com/alexbeloi/nn-holdem) and [rlcard](https://github.com/datamllab/rlcard) were enormously helpful for this project.

#### **Poker and Machine Learning**
##### *Applications in game theory*
* Poker is a type of imperfect information game providing an opportunity to use machine learning agents to find winning strategies.
* Created a simplified Texas Hold'em environment to train a CFR agent.
* The CFR agent showed improved performance over fixed strategy agents (i.e. no learning involved) to win a majority of hands.
* The rlcard repo allowed me to upload my agent and have it play against other AIs.
* Further development:
<ul>-Train the model on real-world poker hand data using LSTM to analyze player trends in series of hands.
<br>-Use image recognition to identify a player's "tells" when they are bluffing.
<br>-Continue to develop a full Texas Hold-em game environment.</ul>
* Reinforcement learning could be applied to any real-world imperfect information situation, like international business or trade negotiations.  Rewards and expected responses could be modeled to determine strategies that maximize rewards.

##### **Resources:**
* rlcard (https://github.com/datamllab/rlcard)
@article{zha2019rlcard,
  title={RLCard: A Toolkit for Reinforcement Learning in Card Games},
  author={Zha, Daochen and Lai, Kwei-Herng and Cao, Yuanpu and Huang, Songyi and Wei, Ruzhe and Guo, Junyu and Hu, Xia},
  journal={arXiv preprint arXiv:1910.04376},
  year={2019}
}
* This article was extremely helpful in constructing my own agent: https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-1-5-contextual-bandits-bff01d1aad9c
* environ setup: https://github.com/alexbeloi/nn-holdem