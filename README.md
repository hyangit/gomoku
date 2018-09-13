# 五子棋

### 模块分析
- **start**: 是游戏入口，可以选择待对战的游戏
- **game**: 是游戏，一个游戏包含一个棋谱，两个玩家，一个显示平台
   - **human_pk_policy_game**: 人类玩家和策略玩家对战
   - **policy_pk_policy_game**: 策略玩家和策略玩家对战
- **chessboard**: 是棋谱，可控制行列数，给定原始棋谱（棋局恢复）
- **player**: 是玩家，总共实现了4中玩家
   - **random_player**: 随机下棋
   - **policy_player**: 策略玩家，通过当前棋谱，计算每一位置的得分（进攻得分&防御得分），分数最高作为最终落子位置
   - **human_player**: 人类玩家，通过在控制台输入坐标，与其他玩家对弈
   - **tkinter_human_player**: GUI玩家，通过在界面的棋谱上点击位置，与其他玩家对弈（依赖**tkinter_display**）
- **display**: 显示平台，显示棋谱和玩家落子的情况（同时还起着督促玩家落子的功能），基类只负责驱动玩家落子
   - **print_display**: 打印机显示平台，将每一步的棋谱打印在控制台上
   - **tkinter_display**: TkinterGUI显示平台，提供界面展示棋谱

---
### 性能分析
共走步数： 86
策略玩家自我对弈一局耗时:  2.333743

---
### 界面截图
![](./screenshots.jpg '界面截图')

---
### TODO
- **minimax_policy_player**: 采用*Minimax+Alpha–beta剪枝*算法和*评分策略*得到最优落子位置
- **MCTS_policy_player**: 采用*模特卡洛搜索*算法和*评分策略*得到最优落子位置
- **MCTS_DQN_player**: 采用*模特卡洛搜索*算法和*DQN强化学习*算法得到最优落子位置
