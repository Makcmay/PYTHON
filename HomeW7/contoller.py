import view
import logger
import model_complex as mc
import model_rational as mr

def clac_start():
    info = view.get_number_info()
    if info == 1:
        value_a = view.get_complex_value()
        value_b = view.get_complex_value()
        action = view.get_action()

        mc.init(value_a, value_b, action)
        result = mc.do_it()
        view.view_data(result, "resalt")


    if info == 2:
        value_a = view.get_float_value()
        value_b = view.get_float_value()
        action = view.get_action()

        mr.init(value_a, value_b, action)
        result = mr.do_it()
        view.view_data(result, "resalt")
        logger.write_log(info, value_a, value_b, action, result)
    else:
        print('ERR')

    
    





