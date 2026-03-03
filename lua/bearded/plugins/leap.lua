local M = {}

function M.highlights(ui, colors)
  return {
    LeapMatch = { bg = colors.blue, fg = ui.defaultMain, bold = true },
    LeapLabel = { fg = colors.blue, bold = true },
    LeapBackdrop = { fg = ui.defaultalt },
  }
end

return M
