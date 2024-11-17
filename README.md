# Multi-Agent System with LangChain and LangGraph

## Overview
This project demonstrates a sophisticated multi-agent system utilizing **LangChain** and **LangGraph** libraries to handle complex tasks involving information retrieval, semantic reasoning, and knowledge base interactions. The system integrates multiple agents, each tailored for specific functionalities, to effectively work with diverse data sources and provide precise answers or insights.

---

## Key Features
1. **Retrieval-Augmented Generation (RAG) Agent**  
   - Extracts and processes information from **unstructured documents**.  
   - Combines retrieval and generation techniques for contextually relevant responses.

2. **Graph Query Agent**  
   - Interfaces with a **Neo4j graph database** to fetch and analyze structured data.  
   - Leverages graph-based insights for advanced knowledge reasoning.

3. **Vector Database Integration**  
   - Enhances semantic search and similarity matching using a **vector database**.

4. **Large Language Model Integration**  
   - Powered by **Llama 3.1 70B versatile** via the **GROQ API** for state-of-the-art natural language understanding and generation.

---

## Architecture
The system consists of the following components:
- **Data Sources**:
  - **Neo4j Graph Database**: Stores and manages structured knowledge.
  - **Vector Database**: Enables high-performance semantic retrieval.
  - **Unstructured Documents**: Serves as a resource for text-based knowledge extraction.
  
- **Agent Interaction Framework**:
  - Facilitated by **LangChain** and **LangGraph**, ensuring smooth and efficient communication between agents.

- **Inference Backend**:
  - Utilizes the Llama 3.1 model for generating intelligent and contextual responses.

### Visual Representations
- **Schematic Architecture**: Displays the system's logical flow.


 ![image](https://github.com/user-attachments/assets/925e4f65-7f3a-4a1e-bfad-b8a2d7d2b86c)
 

- **Graphical Architecture**: Provides a visual representation of component interactions.

![image](https://github.com/user-attachments/assets/4142a055-3f25-416f-8c9a-e3e448f39735)


---

## Requirements
- Python >= 3.8
- Libraries:
  - `LangChain`
  - `LangGraph`
  - `Neo4j`
  - Vector database client (e.g., Pinecone, Weaviate)
  - GROQ API client
- Llama 3.1 model (API key required for GROQ)

---

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/multi-agent-system.git
