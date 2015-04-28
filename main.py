#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Mon Apr 27 21:03:03 2015
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class RootFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: RootFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.checkbox_resize = wx.CheckBox(self, wx.ID_ANY, "Resize")
        self.resize_mode_radio_box = wx.RadioBox(self, wx.ID_ANY, "Mode", choices=["Width and Height", "Long side", "Narrow side"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        # self.resize_mode_radio_box = wx.RadioBox(self, wx.ID_ANY, "Mode", choices=["Height and Width", "Long side"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.label_resize_input_size = wx.StaticText(self, wx.ID_ANY, "Width / Height or Select Side", style=wx.ALIGN_CENTRE)
        self.input_resize_width = wx.TextCtrl(self, wx.ID_ANY, "")
        self.input_resize_height = wx.TextCtrl(self, wx.ID_ANY, "")
        self.checkbox_aspect = wx.CheckBox(self, wx.ID_ANY, "Aspect")
        self.checkbox_zoom = wx.CheckBox(self, wx.ID_ANY, "Zoom")
        self.resample_mode_radio_box = wx.RadioBox(self, wx.ID_ANY, "Resample", choices=["Antialias", "Bicubic", "Bilinear"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.checkbox_colors = wx.CheckBox(self, wx.ID_ANY, "Colors")
        self.combo_box_colors = wx.ComboBox(self, wx.ID_ANY, choices=["24bit", "8bit", "4bit", "1bit"], style=wx.CB_DROPDOWN)
        self.checkbox_flip_holizontal = wx.CheckBox(self, wx.ID_ANY, "Flip Horizontal")
        self.checkbox_flip_vertical = wx.CheckBox(self, wx.ID_ANY, "Flip Vertical")
        self.checkbox_flip_exif = wx.CheckBox(self, wx.ID_ANY, "Flip EXIF")
        self.checkbox_grayscale = wx.CheckBox(self, wx.ID_ANY, "Grayscale")
        self.checkbox_negative = wx.CheckBox(self, wx.ID_ANY, "Flip Negative")
        self.checkbox_file_overwrite = wx.CheckBox(self, wx.ID_ANY, "File Overwrite")
        self.checkbox_output_dir = wx.CheckBox(self, wx.ID_ANY, "Output Dir")
        self.input_output_dir = wx.TextCtrl(self, wx.ID_ANY, "convert")
        self.checkbox_file_format = wx.CheckBox(self, wx.ID_ANY, "File Format")
        self.combo_box_format = wx.ComboBox(self, wx.ID_ANY, choices=["Jpeg", "Png", "Gif"], style=wx.CB_DROPDOWN)
        self.static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        self.tree_filelist = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER | wx.FULL_REPAINT_ON_RESIZE)
        # XXX
        self.tree_filelist.InsertColumn(0, 'filename', wx.LIST_FORMAT_LEFT)
        self.button_file_choose = wx.Button(self, wx.ID_ANY, "Choose")
        self.button_file_convert = wx.Button(self, wx.ID_ANY, "Convert")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.ChangeResizeMode, self.resize_mode_radio_box)
        self.Bind(wx.EVT_BUTTON, self.OnFileChoose, self.button_file_choose)
        self.Bind(wx.EVT_BUTTON, self.OnConvert, self.button_file_convert)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: RootFrame.__set_properties
        self.SetTitle("Pylfan")
        self.SetSize((896, 600))
        self.resize_mode_radio_box.SetSelection(0)
        self.checkbox_aspect.SetValue(1)
        self.resample_mode_radio_box.SetSelection(0)
        self.combo_box_colors.SetSelection(0)
        self.checkbox_output_dir.SetValue(1)
        self.combo_box_format.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RootFrame.__do_layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        sub_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_sizer = wx.BoxSizer(wx.VERTICAL)
        filelist_sizer = wx.BoxSizer(wx.HORIZONTAL)
        filelist_sub_sizer = wx.BoxSizer(wx.VERTICAL)
        file_buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_overwrite_sizer = wx.BoxSizer(wx.VERTICAL)
        file_format_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_output_sizer = wx.BoxSizer(wx.HORIZONTAL)
        convert_sizer = wx.BoxSizer(wx.VERTICAL)
        colors_select_sizer = wx.BoxSizer(wx.HORIZONTAL)
        edit_sizer = wx.BoxSizer(wx.VERTICAL)
        zoom_sizer = wx.BoxSizer(wx.VERTICAL)
        resize_sizer = wx.BoxSizer(wx.VERTICAL)
        resize_input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        resize_sizer.Add(self.checkbox_resize, 0, wx.EXPAND, 0)
        resize_sizer.Add(self.resize_mode_radio_box, 0, wx.EXPAND, 0)
        resize_sizer.Add(self.label_resize_input_size, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        resize_input_sizer.Add(self.input_resize_width, 0, 0, 0)
        resize_input_sizer.Add(self.input_resize_height, 0, 0, 0)
        resize_sizer.Add(resize_input_sizer, 1, wx.SHAPED, 0)
        edit_sizer.Add(resize_sizer, 1, wx.EXPAND, 0)
        zoom_sizer.Add(self.checkbox_aspect, 0, wx.EXPAND, 0)
        zoom_sizer.Add(self.checkbox_zoom, 0, wx.EXPAND, 0)
        zoom_sizer.Add(self.resample_mode_radio_box, 0, wx.EXPAND, 0)
        edit_sizer.Add(zoom_sizer, 1, wx.EXPAND, 0)
        sub_sizer.Add(edit_sizer, 1, 0, 0)
        colors_select_sizer.Add(self.checkbox_colors, 0, 0, 0)
        colors_select_sizer.Add(self.combo_box_colors, 0, 0, 0)
        convert_sizer.Add(colors_select_sizer, 1, wx.EXPAND | wx.SHAPED, 0)
        convert_sizer.Add(self.checkbox_flip_holizontal, 0, wx.EXPAND, 0)
        convert_sizer.Add(self.checkbox_flip_vertical, 0, wx.EXPAND, 0)
        convert_sizer.Add(self.checkbox_flip_exif, 0, wx.EXPAND, 0)
        convert_sizer.Add(self.checkbox_grayscale, 0, wx.EXPAND, 0)
        convert_sizer.Add(self.checkbox_negative, 0, wx.EXPAND, 0)
        sub_sizer.Add(convert_sizer, 1, 0, 0)
        file_overwrite_sizer.Add(self.checkbox_file_overwrite, 0, wx.EXPAND, 0)
        file_output_sizer.Add(self.checkbox_output_dir, 0, 0, 0)
        file_output_sizer.Add(self.input_output_dir, 0, 0, 0)
        file_overwrite_sizer.Add(file_output_sizer, 1, 0, 0)
        file_format_sizer.Add(self.checkbox_file_format, 0, 0, 0)
        file_format_sizer.Add(self.combo_box_format, 0, 0, 0)
        file_overwrite_sizer.Add(file_format_sizer, 1, 0, 0)
        file_sizer.Add(file_overwrite_sizer, 1, 0, 0)
        file_sizer.Add(self.static_line_2, 0, wx.EXPAND, 0)
        filelist_sub_sizer.Add(self.tree_filelist, 1, wx.EXPAND, 0)
        file_buttons_sizer.Add(self.button_file_choose, 0, 0, 0)
        file_buttons_sizer.Add(self.button_file_convert, 0, 0, 0)
        filelist_sub_sizer.Add(file_buttons_sizer, 1, 0, 0)
        filelist_sizer.Add(filelist_sub_sizer, 1, 0, 0)
        file_sizer.Add(filelist_sizer, 1, wx.EXPAND, 0)
        sub_sizer.Add(file_sizer, 1, 0, 0)
        main_sizer.Add(sub_sizer, 1, wx.EXPAND, 0)
        self.SetSizer(main_sizer)
        self.Layout()
        # end wxGlade

    def ChangeResizeMode(self, event):  # wxGlade: RootFrame.<event_handler>
        # XXX
        selection = self.resize_mode_radio_box.GetSelection()
        if 1 == selection or 2 == selection:
            self.input_resize_height.Disable()
        else:
            self.input_resize_height.Enable()

    def OnFileChoose(self, event):  # wxGlade: RootFrame.<event_handler>
        dialog = wx.FileDialog(self, 'Choose files', './', '', 'Image files (*.gif;*.png;*.jpg)|*.gif;*.png;*.jpg;*.JPG', wx.FD_MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            self.convert_files = dialog.GetFilenames()
            self.convert_file_dir = dialog.GetDirectory()
        else:
            dialog.Destroy()
            return
        dialog.Destroy()

        for i, convert_file in enumerate(self.convert_files):
            self.tree_filelist.InsertStringItem(i, convert_file)

    def OnConvert(self, event):  # wxGlade: RootFrame.<event_handler>
        import PIL.ImageOps
        import Image
        import shutil
        import glob
        import time
        import os
        import sys

        is_resize = self.checkbox_resize.IsChecked()
        resize_mode = self.resize_mode_radio_box.GetSelection()
        width = int(self.input_resize_width.GetValue())
        if resize_mode == 0:
            height = int(self.input_resize_height.GetValue())
        else:
            height = None
        is_aspect = self.checkbox_aspect.IsChecked()
        is_zoom = self.checkbox_zoom.IsChecked()
        resample_mode = self.resample_mode_radio_box.GetSelection()

        is_colors = self.checkbox_colors.IsChecked()
        color_mode = self.combo_box_colors.GetSelection()
        is_flip_horizontal = self.checkbox_flip_holizontal.IsChecked()
        is_flip_vertical = self.checkbox_flip_vertical.IsChecked()
        is_flip_exif = self.checkbox_flip_exif.IsChecked()
        is_grayscale = self.checkbox_grayscale.IsChecked()
        is_flip_negative = self.checkbox_negative.IsChecked()

        is_file_overwrite = self.checkbox_file_overwrite.IsChecked()
        is_file_output_dir = self.checkbox_output_dir.IsChecked()
        file_output_dir = self.input_output_dir.GetValue()
        is_file_format = self.checkbox_file_format.IsChecked()
        file_format = self.combo_box_format.GetSelection()

        RESAMPLE_MODES = [Image.ANTIALIAS, Image.BICUBIC, Image.BILINEAR]
        FORMATS = ['JPEG', 'PNG', 'GIF']

        tmp_dir = os.path.join('/tmp', 'pylfan-'+str(time.time()))
        os.mkdir(tmp_dir)
        # backup original files
        for convert_file in self.convert_files:
            current_file = os.path.join(self.convert_file_dir, convert_file)
            shutil.copy(current_file, tmp_dir)

            image = Image.open(os.path.join(tmp_dir, convert_file))

            if is_flip_exif:
                convert_image = {
                    1: lambda img: img,
                    2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),
                    3: lambda img: img.transpose(Image.ROTATE_180),
                    4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),
                    5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90),
                    6: lambda img: img.transpose(Image.ROTATE_270),
                    7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270),
                    8: lambda img: img.transpose(Image.ROTATE_90),
                }
                exif = image._getexif()
                orientation = exif.get(0x112, 1)
                image = convert_image[orientation](image)

            if is_resize:
                if (width >= image.size[0] and height >= image.size[1]) and not is_zoom:
                    pass
                else:
                    if resize_mode == 0:
                        if is_aspect:
                            wpercent = (width/float(image.size[0]))
                            hpercent = (height/float(image.size[1]))
                            if wpercent <= hpercent:
                                hsize = int((float(image.size[1]) * float(wpercent)))
                                image = image.resize((width, hsize), RESAMPLE_MODES[resample_mode])
                            else:
                                wsize = int((float(image.size[0]) * float(hpercent)))
                                image = image.resize((wsize, height), RESAMPLE_MODES[resample_mode])
                        else:
                            image = image.resize((height, width), RESAMPLE_MODES[resample_mode])
                    elif resize_mode == 1:
                        wpercent = (width/float(image.size[0]))
                        hpercent = (width/float(image.size[1]))
                        if wpercent <= hpercent:
                            hsize = int((float(image.size[1]) * float(wpercent)))
                            image = image.resize((width, hsize), RESAMPLE_MODES[resample_mode])
                        else:
                            wsize = int((float(image.size[0]) * float(hpercent)))
                            image = image.resize((wsize, width), RESAMPLE_MODES[resample_mode])
                    elif resize_mode == 2:
                        wpercent = (width/float(image.size[0]))
                        hpercent = (width/float(image.size[1]))
                        if wpercent >= hpercent:
                            hsize = int((float(image.size[1]) * float(wpercent)))
                            image = image.resize((width, hsize), RESAMPLE_MODES[resample_mode])
                        else:
                            wsize = int((float(image.size[0]) * float(hpercent)))
                            image = image.resize((wsize, width), RESAMPLE_MODES[resample_mode])

            if is_flip_horizontal:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)

            if is_flip_vertical:
                image = image.transpose(Image.FLIP_TOP_BOTTOM)

            if is_grayscale:
                image = image.convert('L')

            if is_flip_negative:
                image = PIL.ImageOps.invert(image)

            # XXX add quality control
            if is_file_format:
                new_filename = '.'.join(convert_file.split('.')[:-1])+'.{0}'.format(FORMATS[file_format].lower())
                image.save(os.path.join(tmp_dir, new_filename), FORMATS[file_format], quality=85)
            else:
                image.save(os.path.join(tmp_dir, convert_file), quality=85, )

        if is_file_output_dir:
            move_dir = os.path.join(self.convert_file_dir, file_output_dir)
            if not os.path.exists(move_dir):
                os.mkdir(move_dir)
        elif is_file_overwrite:
            move_dir = file_output_dir
        else:
            print 'make file an {0} directory'.format(tmp_dir)
            sys.exit()

        for file_path in glob.glob(os.path.join(tmp_dir, '*')):
            shutil.copy(file_path, move_dir)



# end of class RootFrame


class PylfanApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        root_frame = RootFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(root_frame)
        root_frame.Show()
        return 1
# end of class PylfanApp


if __name__ == "__main__":
    Pylfan = PylfanApp(0)
    Pylfan.MainLoop()