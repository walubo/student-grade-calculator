# Git Reflection

**Student Name:** Aries R. Magto  
**Section:** [Your Section Here]  
**Course Assignment:** Individual Git & GitHub Repository  

---

### Reflection: Resolving a Merge Conflict During Branch Integration

During this assignment, the most challenging issue I encountered in Git was resolving a merge conflict while merging my feature branch into the main branch. After implementing the input validation and GPA scaling system on my feature branch, I realized that I had also modified the main script's output formatting directly on the main branch. When I ran `git merge`, Git halted the operation and flagged conflicting changes in `grade_calculator.py`.

At first, seeing the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) was intimidating because I was worried about losing working code. To solve this, I opened the conflicting file in my code editor, carefully compared the two versions, and determined how to combine both improvements. I chose to preserve the updated validation logic from the feature branch while keeping the cleaner output layout from the main branch. Once the markers were removed, I tested the script to verify everything worked as expected, staged the resolved file using `git add`, and finalized the merge with a clean commit. This experience taught me how Git manages parallel changes and boosted my confidence in navigating branch workflows.
