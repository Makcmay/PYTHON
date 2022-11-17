import view
import logger
import model

def calc_start():
    while True:
        try:
            info = view.get_number_info()
            view.new_line()
            if info == 1:
                value_a = view.get_complex_value()
                value_b = view.get_complex_value()
                action = view.get_action()
            elif info == 2:
                value_a = view.get_float_value()
                value_b = view.get_float_value()
                action = view.get_action()
            elif info == 3:
                break
            else:
                view.menu_error()
                continue
            view.new_line()
            model.init(value_a, value_b, action)
            result = model.do_it()
            view.view_data(result, value_a, value_b, action)
            logger.write_log(info, value_a, value_b, action, result)
            view.new_line()
        except:
            view.menu_error()
            view.new_line()
    




