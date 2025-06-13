# Task 2 - Data Version Control (DVC)

In regulated industries like insurance, it's critical to track not just code but also data. **Task 2** focuses on establishing reproducible, auditable pipelines by using **DVC** (Data Version Control).

## ✅ Objectives

* Set up DVC for data versioning
* Configure a local remote data store
* Track the raw insurance dataset
* Push data to the remote

## 🧰 Tools Used

* [DVC](https://dvc.org/) – open-source tool for versioning data, models, and pipelines
* Git – to track code and DVC metadata

## 🗂️ Repository Structure Update

```
insurance-challenge-week/
├── .dvc/                     # DVC internal config files
├── data/
│   ├── MachineLearningRating_v3.csv          # Raw dataset (Git-ignored)
│   └── MachineLearningRating_v3.csv.dvc      # DVC tracking metadata
├── dvc.yaml                 # Will be added in Task 4 (pipeline)
└── scripts/
    └── task-2.sh            # Shell script for setting up DVC
```

## 🔧 Setup Steps (Automated in `task-2.sh`)

1. **Initialize DVC**
2. **Create and configure a local remote** at `/mnt/data/dvc-storage`
3. **Track the dataset** using `dvc add`
4. **Push to remote** using `dvc push`

To run the automation:

```bash
bash scripts/task-2.sh
```

## 💡 Why DVC?

* 🕵️ Reproducibility: You can always re-run models with the exact data version used
* 🔐 Compliance: Satisfies auditing and regulatory requirements
* 📦 Scalability: Handles large datasets without storing them in Git

## ✅ Final Checklist

* [x] `dvc init`
* [x] Local remote created and configured
* [x] Dataset tracked and `.dvc` file committed
* [x] Data pushed to remote

---

**Author**: Lidet Teshome - lidet.teshome.aastu@gmail.com  
**Week**: B5W3 – Insurance Risk & Predictive Analytics Challenge
