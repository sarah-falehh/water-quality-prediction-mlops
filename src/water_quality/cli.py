import argparse

from .config import DATA_PATH, MODEL_PATH
from .pipeline import save_model, train_and_evaluate


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the water-potability classifier.")
    parser.add_argument("--data", default=str(DATA_PATH))
    parser.add_argument("--model-path", default=str(MODEL_PATH))
    parser.add_argument("--n-estimators", type=int, default=300)
    parser.add_argument("--max-depth", type=int, default=None)
    args = parser.parse_args()

    model, accuracy, _, _ = train_and_evaluate(
        args.data, n_estimators=args.n_estimators, max_depth=args.max_depth
    )
    save_model(model, args.model_path)
    print(f"Model saved to {args.model_path}; test accuracy={accuracy:.4f}")


if __name__ == "__main__":
    main()
