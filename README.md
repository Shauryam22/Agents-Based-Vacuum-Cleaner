# AI Agents Simulation – Vacuum Cleaner World

This project simulates different types of **AI agents** in a simple **grid-based environment** where the agent must clean dirty cells (`D`), avoid walls (`#`), and try to maximize performance.  

The code demonstrates concepts from **Artificial Intelligence agent design**:  
- Simple Reflex Agent  
- Model-Based Reflex Agent  
- Goal-Based Agent  
- Utility-Based Agent  
- Learning Agent  

---

## 🗂 Project Structure
- **environment class**: Defines the 4x4 grid world with dirt (`D`), clean (`C`), and blocked (`#`) cells. Handles agent movement, cleaning actions, and performance measurement.  
- **Agent classes**:
  - `Simple_reflex`: Acts only based on current percept.  
  - `Model_based`: Maintains an internal model of the environment.  
  - `Goal_based_agent`: Acts to achieve a goal (all clean).  
  - `utility_based_agent`: Uses a utility function to decide actions.  
  - `Learning_agent`: Improves decisions using past experiences.  
- **simulate() function**: Runs the environment for a chosen agent for a given number of steps.  

---

## ⚙️ How It Works
1. The environment starts with some **dirty cells (`D`)**, clean cells (`C`), and blocked cells (`#`) arranged in a grid.  
2. Each agent receives a **percept** (the current cell state).  
3. The agent chooses an **action**:
   - `C` → Clean the cell.  
   - `move` → Move to a neighbor cell.  
4. The environment updates, assigns a **performance measure**, and continues until all cells are clean.  

---

## 🚀 Usage
Run the script directly:

```bash
python agents_simulation.py
