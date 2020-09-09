def exit(code = 0):
    sys.exit(0)
    
is_main = mod.is_main
init_logger = log.init_logger

def get_temp_path(name = ''):
    _count = get_count();
    path = '~/temp/no-use/images/%s_%d_%s.png'%(log.get_date_str(), _count, name)
    return path
def sit(img = None, format = 'rgb', path = None, name = ""):
    if path is None:
        path = get_temp_path(name)
        
    if img is None:
        plt.save_image(path)
        return path
    
        
    if format == 'bgr':
        img = _img.bgr2rgb(img)
    if type(img) == list:
        plt.show_images(images = img, path = path, show = False, axis_off = True, save = True)
    else:
        plt.imwrite(path, img)
    
    return path
_count = 0;

def get_count():
    global _count;
    _count += 1;
    return _count    

def cit(img, path = None, rgb = True, name = ""):
    _count = get_count();
    if path is None:
        img = np.np.asarray(img, dtype = np.np.uint8)
        path = '~/temp/no-use/images/%s_%s_%d.jpg'%(name, log.get_date_str(), _count)
        _img.imwrite(path, img, rgb = rgb)
    return path        

argv = sys.argv