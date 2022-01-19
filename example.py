import argparse, sys
import exp_manager as EM

if __name__ == "__main__":
    def parse_args():
        parser = argparse.ArgumentParser(description="Example")
        parser.add_argument("--path", type=str, help="path to save the results and file")
        parser.add_argument("--param", type=str, help="a random param")
        return parser.parse_args()
   
    args = parse_args()
    # put this line at the beginning, you can modify the postfix to specify how you want to name your folder
    expr = EM.ExprManager(args.path, postfix="param%.1f" % (int(args.param)))

    # do your experiment
    import config
    print(config.var0)

    # call this at the end of the file
    # if you have a trained model you can choose to save it in the same directory
    # expr.save_model(model)
    expr.dump_src_code_and_model_def(sys.argv[0])

